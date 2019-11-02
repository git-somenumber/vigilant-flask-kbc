from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


files = Config()
app = Flask(__name__)
app.config.from_object(files)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
