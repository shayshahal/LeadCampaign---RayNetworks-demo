import os
from facebook_business.api import FacebookAdsApi
from flask import Flask
from flask_migrate import Migrate
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .controller import graphql_blueprint
    app.register_blueprint(graphql_blueprint)

    from .models import db
    db.init_app(app)

    migrate = Migrate()
    migrate.init_app(app)

    FacebookAdsApi.init(access_token=os.environ['ACCESS_TOKEN'])
    
    return app