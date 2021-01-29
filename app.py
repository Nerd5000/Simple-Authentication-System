from flask import Flask, request
from controllers.jwtcontroller import token_valid
from routes.auth import auth
from models.dbfile import db

app = Flask(__name__)

app.register_blueprint(auth)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/secret')
def secret():
    jwt = request.json
    auth = token_valid(jwt['jwt'])
    if auth[2]:
        return '{}'.format(auth[1])
    else:
        return 'Sorry Invalid Json'.format(auth[1])


@app.route('/')
def main():
    from models.user import User
    from models.blockedJWT import BlockedJWT
    db.create_all()
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
