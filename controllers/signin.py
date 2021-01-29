from controllers.check_credentials import CheckCredentials
from controllers.hashing import hash_password_salt
from controllers.jwtcontroller import encode_auth_token, decode_auth_token
from models.user import User
from models.dbfile import db


class SignIn:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def checkUser(self):
        if CheckCredentials().checkmail(self.email):
            password = db.session.query(User.password).filter_by(
                email=self.email).scalar()
            salt = db.session.query(User.salt).filter_by(
                email=self.email).scalar()
            if password != None:
                hashed_password = hash_password_salt(self.password, salt)
                if password == hashed_password:
                    jwt = encode_auth_token(self.email)
                    return str({'jwt': jwt})
                else:
                    return 401
            else:
                return 'Email Not Exist'
