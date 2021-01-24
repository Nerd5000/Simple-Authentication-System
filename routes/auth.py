from flask import Blueprint, request
from controllers.signup import SignUp
from controllers.signin import SignIn
from controllers.logout import Logout

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['POST'])
def signup():
    user = request.json
    if user['email'] != None and user['password'] != None:
        sign = SignUp(user['email'].lower(), user['password'])
        return sign.createUser()
    else:
        return 'Invalid Json'


@auth.route('/signin', methods=['POST'])
def signin():
    user = request.json
    if user['email'] != None and user['password'] != None:
        sign = SignIn(user['email'].lower(), user['password'])
        return sign.checkUser()
    else:
        return 'Invalid Json'


@auth.route('/logout', methods=['POST'])
def logout():
    json_data = request.json
    if json_data['jwt'] != None:
        logout = Logout(json_data['jwt'])
        return logout.logout()
    else:
        return 'Invalid Json'
