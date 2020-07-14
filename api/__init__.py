from flask import Flask
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# instantiate db object
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    migrate = Migrate(app, db)
    app.config['CORS_HEADERS'] = 'Content-Type'

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
# instantiate app
    db.init_app(app)

    # blueprint for auth routes in app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .views import api
    app.register_blueprint(api)

    return app
