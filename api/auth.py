from flask import Blueprint
from . import db

auth= Blueprint('auth', __name__)


@auth.route('/logged_in')
def login():
    return 'Logged In!'


@auth.route('/signup')
def signup():
    return 'Signup'


@auth.route('/logout')
def logout():
    return 'Logout'
