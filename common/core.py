from flask import Flask
from flask.ext.mongoengine import MongoEngine
import tools

# Contains the main shared instances between the app and the api
app = Flask(__name__)
app.config.from_object('config')
app.debug = True

# Flask-MongoEngine instance
db = MongoEngine(app)

# Custom Converters
app.url_map.converters['objectid'] = tools.ObjectIDConverter