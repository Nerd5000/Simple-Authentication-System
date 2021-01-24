from models.dbfile import db


class BlockedJWT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jwt = db.Column(db.String())

    def __init__(self, jwt):
        self.jwt = jwt
