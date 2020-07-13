from flask import Blueprint, jsonify, request
import requests
from . import db
from .models import job_listings
from .models import site_users
import pdb

api = Blueprint('api', __name__)
BASE_URL = 'https://jobs.github.com/positions.json?'


# add user to db
@api.route("/add_user", methods=['POST'])
def add_user():
    user_data = request.get_json()
    new_user = site_users(name=user_data['name'])

    db.session.add(new_user)
    db.session.commit()

    return 'User Successfully Added', 201


@api.route("/users")
def users():
    # query db table
    user_list = site_users.query.all()
    users = []

    for user in user_list:
        users.append({'name': user.name})

    return jsonify({'users': users})


@api.route("/add_job_listing", methods=['POST'])
def add_job_listing():
    job_listing_data = request.get_json()
    new_job_listing = job_listings(external_id=job_listing_data['external_id'], name=job_listing_data['name'], created_at=job_listing_data['created_at'], company=job_listing_data['company'],
                                   company_url=job_listing_data['company_url'], location=job_listing_data['location'], title=job_listing_data['title'], description=job_listing_data['description'])

    db.session.add(new_job_listing)
    db.session.commit()

    return 'User Successfully Added', 201


@api.route('/job_listings')
def joblistings():
    description = request.args.get('description')
    location = request.args.get('location')
    response = requests.get(
        BASE_URL, params={'location': location, 'description': description})

    job_list = response.json()

    jobs = []
    for listing in job_list:
        jobs.append({'company': listing['company'], 'title': listing['title'],
                     'location': listing['location']})

    return jsonify({'jobs': jobs})
 