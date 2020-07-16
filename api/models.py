from . import db


class user_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(75), nullable=False)
    password = db.Column(db.String(50), nullable=False)


class job_listings(db.Model):
    id = db.Column(db.Integer, nullable=False)
    external_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.String(50), nullable=False)
    company = db.Column(db.String(75), nullable=False)
    company_url = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
