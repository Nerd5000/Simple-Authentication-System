import hashlib
import uuid


def hash_password(password):
    salt = uuid.uuid4().hex
    salted_password = password+salt
    hashed_password = hashlib.sha512(
        salted_password.encode('utf-8')).hexdigest()
    return [hashed_password, salt]


def hash_password_salt(password, salt):
    salted_password = password+salt
    hashed_password = hashlib.sha512(
        salted_password.encode('utf-8')).hexdigest()
    return hashed_password
