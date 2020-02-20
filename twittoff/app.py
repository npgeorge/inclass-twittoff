import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from twittoff.models import db, User, Tweet, migrate
from twittoff.routes import my_routes
#from twittoff.more_routes import more_routes
from twittoff.twitter_service import twitter_api_client

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", default="OOPS")

def create_app():
    app = Flask(__name__)
    app.config["CUSTOM_VAR"] = 5 # just an example of app config :-D
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///web_app_200.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["TWITTER_API_CLIENT"] = twitter_api_client()

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(my_routes)
    #app.register_blueprint(more_routes)

    return app

#reset route from class
#@new_routes.route("/reset")
#def reset():
#    db.drop_all()
#    db.create_all()
#    return jsonify({"message": "Database Reset OK"})