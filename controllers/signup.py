from controllers.check_credentials import CheckCredentials
from controllers.hashing import hash_password
from models.user import User
from models.dbfile import db


class SignUp:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def createUser(self):
        if CheckCredentials().checkmail(self.email):
            hashed_password = hash_password(self.password)
            try:
                user = User(self.email, hashed_password[0], hashed_password[1])
                db.session.add(user)
                db.session.commit()
                return 'created'
            except Exception as e:
                # return str(e.__class__)
                return 'Email Already resgistred'
        else:
            return 'Not an Email'
