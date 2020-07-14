from flask import Blueprint
from . import db

auth = Blueprint('auth', __name__)

# add user to db
# @auth.route("/registrations", methods=['POST'])
# def registration():
#     user_data = request.get_json()
#     new_user = site_users(name=user_data['name'])

#     db.session.add(new_user)
#     db.session.commit()

#     return 'User Successfully Added', 201
#     return 'Registrations'


@auth.route('/login')
def login():
    return 'Login'


@auth.route('/signup')
def signup():
    return 'Signup'


@auth.route('/logout')
def logout():
    return 'Logout'
