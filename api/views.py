from flask import Blueprint, jsonify, request
import requests
from . import db
from flask_cors import CORS, cross_origin
from .models import job_listings
from .models import site_users
import pdb

api_v1 = Blueprint('api_v1', __name__)

CORS(api_v1)

BASE_URL = 'https://jobs.github.com/positions.json?'


# add user to db
@api_v1.route("/api/v1/users/registrations", methods=['POST'])
@cross_origin()

def add_user():
    user_data = request.get_json()
    new_user = site_users(name=user_data['name'])

    db.session.add(new_user)
    db.session.commit()

    return 'User Successfully Added', 201


@api_v1.route("/users")
@cross_origin()

def users():
    # query db table
    user_list = site_users.query.all()
    users = []

    for user in user_list:
        users.append({'name': user.name})

    return jsonify({'users': users})


@api_v1.route("/api/v1/add_job_listing", methods=['POST'])
@cross_origin()

def add_job_listing():
    job_listing_data = request.get_json()
    new_job_listing = job_listings(external_id=job_listing_data['external_id'], name=job_listing_data['name'], created_at=job_listing_data['created_at'], company=job_listing_data['company'],
                                   company_url=job_listing_data['company_url'], location=job_listing_data['location'], title=job_listing_data['title'], description=job_listing_data['description'])

    db.session.add(new_job_listing)
    db.session.commit()

    return 'Job Successfully Added', 201


@api_v1.route('/job_listings')
@cross_origin()

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
 