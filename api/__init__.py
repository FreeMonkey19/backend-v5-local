from flask import Flask
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import flask_login
from flask import Response


# instantiate db object
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    cors = CORS(app, supports_credentials=True)

    migrate = Migrate(app, db)
    app.config['CORS_HEADERS'] = 'Content-Type'

    app.config['SECRET_KEY'] = "SECRET KEY (GOES HERE"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
    # instantiate app
    db.init_app(app)

    login_manager = flask_login.LoginManager()
    login_manager.login_view = 'api.login'
    login_manager.init_app(app)
    from .models import user_data

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return user_data.query.get(int(user_data.id))

    from .views import api
    app.register_blueprint(api)

    return app
