from flask import Blueprint, jsonify, request
import requests
from flask import Response
from . import db
from flask_cors import CORS, cross_origin
from .models import job_listings
from .models import user_data
import pdb

api = Blueprint('api', __name__)


CORS(api)

BASE_URL = 'https://jobs.github.com/positions.json?'


# new user
@api.route("/api/users/registrations", methods=['POST'])
@cross_origin()
def add_user():
    new_user_data = request.get_json()

# if this returns a user, email already taken
    user = user_data.query.filter_by(
        email=new_user_data['user']['email']).first()

    if user:

        return Response("{'error': 'user already exists'}",  status=400, mimetype='application/json')

    new_user = user_data(name=new_user_data['user']['name'], email=new_user_data['user']['email'],
                         password=new_user_data['user']['password'], password_confirmation=new_user_data['user']['password_confirmation'])

    db.session.add(new_user)
    db.session.commit()

    return 'User Successfully Registered', 201


# returning user
@api.route("/api/users/login", methods=['POST'])
def login():
    email = request.get_json('email')
    password = request.get_json('password')
    # remember = True if request.get_json('remember') else False

    user = user_data.query.filter_by(email=email).first

    # check if user exists
    # take user password, hash it and compare it to hashed password in db

    if not user:

        return Response("{'error': 'error'}",  status=400, mimetype='application/json')

        login(user, email=user['user']['email'])

    return Response("{'status': 'ok'}",  status=200, mimetype='application/json')


@api.route("/api/users")
@cross_origin()
def users():
    # query db table
    user_list = user_data.query.all()
    users = []

    for user in user_list:
        users.append({'name': user.name, 'email': user.email, 'password': user.password,
                      'password_confirmation': user.password_confirmation})

    return jsonify({'users': users})


# add job listing to db
@ api.route("/api/add_job_listing", methods=['POST'])
@ cross_origin()
def add_job_listing():
    job_listing_data = request.get_json()
    new_job_listing = job_listings(id=job_listing_data['external_id'], title=job_listing_data['title'], created_at=job_listing_data['created_at'], company=job_listing_data['company'],
                                   company_url=job_listing_data['company_url'], location=job_listing_data['location'], description=job_listing_data['description'])

    db.session.add(new_job_listing)
    db.session.commit()

    return 'Job Successfully Added', 201


# get all job listings from api
@ api.route('/api/job_listings')
@ cross_origin()
def joblistings():
    description = request.args.get('description')
    location = request.args.get('location')
    response = requests.get(
        BASE_URL, params={'location': location, 'description': description})

    job_list = response.json()

    jobs = []
    for listing in job_list:
        jobs.append({'id': listing['id'], 'company': listing['company'], 'title': listing['title'], 'created_at': listing['created_at'],
                     'company_url': listing['company_url'], 'location': listing['location'], 'description': listing['description'], 'how_to_apply': listing['how_to_apply'], 'company_logo': listing['company_logo']})

    return jsonify({'jobs': jobs})

    api.route('/api/logout')

    @login_required
    def logout():
        logout_user()

        return Response("{'status': 'successfully logged out'}",  status=200, mimetype='application/json')
