from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

api = Flask(__name__)
api.config.from_object(Config)
CORS(api, resources={r"/*": {"origins": "https://app-razerx100.herokuapp.com/"}})
db = SQLAlchemy(api)
migrate = Migrate(api, db)

from app import endpoints, models