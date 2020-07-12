from flask import Blueprint, jsonify, request
# import requests
from . import db
# from .models import Jobs
# from .models import Users
import pdb

api = Blueprint('api', __name__)
# BASE_URL = 'https://jobs.github.com/positions.json?'


# add user to db
@api.route("/add_user", methods=['POST'])
def add_user():
    # user_data = request.get_json()
    # new_user = Users(name=user_data['name'])

    # db.session.add(new_user)
    # db.session.commit()

    return 'User Successfully Added', 201


@api.route("/users")
def users():
    # user_list = User.query.all()

    users = []

    # for user in user_list:
    #     users.append({'name': users.name})

    return jsonify({'users': users})


# @api.route('/job_listings')
# def joblistings():
#     response = requests.get(BASE_URL)
#     job_list = response.json()
#     # check if request has any request.args
#     # if yes, print args
#     jobs = []
#     for listing in job_list:
#         # if there is location arg then only add listing that matches that location
#         jobs.append({'title' : listing['title'], 'location' : listing['location']})

#     return jsonify({'jobs' : jobs})
