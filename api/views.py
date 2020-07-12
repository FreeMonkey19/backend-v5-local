from flask import Blueprint, jsonify, request
# import requests
from . import db
from .models import JobListings
from .models import SiteUsers
import pdb

api = Blueprint('api', __name__)
# BASE_URL = 'https://jobs.github.com/positions.json?'


# add user to db
@api.route("/add_user", methods=['POST'])
def add_user():
    user_data = request.get_json()
    new_user = SiteUsers(name=user_data['name'])

    db.session.add(new_user)
    db.session.commit()

    return 'User Successfully Added', 201


@api.route("/users")
def users():
    # query db table
    user_list = SiteUsers.query.all()
    users = []
 
    for user in user_list:
        users.append({'name': user.name})

    return jsonify({'users': users})

# @api.route("/add_job_listing", methods=['POST'])
# def add_job_listing():
#     job_listing_data = request.get_json()
#     new_job_listing = SiteUsers(name=user_data['name'])

#     # db.session.add(new_user)
#     # db.session.commit()

#     return 'User Successfully Added', 201


# @api.route("/job_listings")
# def job_listings():
#     # user_list = User.query.all()

#     job_listings = []

    # for user in user_list:
    #     users.append({'name': users.name})

    # return jsonify({'job_listings': job_listings})


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
