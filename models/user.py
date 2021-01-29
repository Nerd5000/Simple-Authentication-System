from models.dbfile import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    salt = db.Column(db.String())

    def __init__(self, email, password, salt):
        self.email = email
        self.password = password
        self.salt = salt
