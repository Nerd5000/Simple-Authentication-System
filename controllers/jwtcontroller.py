import jwt
import datetime
from models.blockedJWT import BlockedJWT
from models.dbfile import db


def encode_auth_token(email):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'sub': email
        }
        return jwt.encode(
            payload,
            'key',
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, 'key', algorithms="HS256")
        return [True, payload['sub']]
    except jwt.ExpiredSignatureError:
        return [False, 'Signature expired. Please log in again.']
    except jwt.InvalidTokenError:
        return [False, 'Invalid token. Please log in again.']


def token_valid(auth_token):
    token_data = decode_auth_token(auth_token)
    if token_data[0]:
        exist = db.session.query(BlockedJWT.id).filter_by(
            jwt=auth_token).scalar() != None
        if exist:
            return [token_data[0], 'You\'ve Logged out', True]
        else:
            return [token_data[0], token_data[1], True]
    else:
        return [token_data[0], token_data[1], False]
