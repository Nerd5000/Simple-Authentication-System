from models.blockedJWT import BlockedJWT
from models.dbfile import db


class Logout:
    def __init__(self, jwt):
        self.jwt = jwt

    def logout(self):
        try:
            jwt = BlockedJWT(self.jwt)
            db.session.add(jwt)
            db.session.commit()
            return 'loged out'
        except:
            return 'Not logged out'
