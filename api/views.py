from flask import Blueprint, jsonify, request
import requests
from . import db
from flask_cors import CORS, cross_origin
from .models import job_listings
from .models import site_users
import pdb

api = Blueprint('api', __name__)

CORS(api)

BASE_URL = 'https://jobs.github.com/positions.json?'


# add user to db
@api.route("/api/users/registrations", methods=['POST'])
@cross_origin()
def add_user():
    user_data = request.get_json()
    new_user = site_users(name=user_data['user']['name'])
    print('hello')
    print(new_user)

    # for value in user_data.values():
    #     print(value)
    #     if value['name'] in user_data:
    #         user_data[value['name']].update(value)
    #     else:
    #         user_data[value['name']] = value

    db.session.add(new_user)
    db.session.commit()

    return 'User Successfully Added', 201


@api.route("/api/users")
@cross_origin()
def users():
    # query db table
    user_list = site_users.query.all()
    users = []

    for user in user_list:
        users.append({'name': user.name})

    return jsonify({'users': users})


@api.route("/api/add_job_listing", methods=['POST'])
@cross_origin()
def add_job_listing():
    job_listing_data = request.get_json()
    new_job_listing = job_listings(external_id=job_listing_data['external_id'], title=job_listing_data['title'], created_at=job_listing_data['created_at'], company=job_listing_data['company'],
                                   company_url=job_listing_data['company_url'], location=job_listing_data['location'], description=job_listing_data['description'])

    db.session.add(new_job_listing)
    db.session.commit()

    return 'Job Successfully Added', 201


@api.route('/api/job_listings')
@cross_origin()
def joblistings():
    description = request.args.get('description')
    location = request.args.get('location')
    response = requests.get(
        BASE_URL, params={'location': location, 'description': description})

    job_list = response.json()

    jobs = []
    for listing in job_list:
        jobs.append({ 'id': listing['id'], 'company': listing['company'], 'title': listing['title'], 'created_at': listing['created_at'],
                     'company_url': listing['company_url'], 'location': listing['location'], 'description': listing['description'], 'how_to_apply': listing['how_to_apply'], 'company_logo': listing['company_logo']})

    return jsonify({'jobs': jobs})
