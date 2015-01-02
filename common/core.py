from flask import Flask
from . import tools
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()

def setup_app(name):
    app = Flask(name)
    app.config.from_object('config')
    app.debug = True

    # Flask-MongoEngine instance
    db.init_app(app)
    
    # Custom Converters
    app.url_map.converters['objectid'] = tools.ObjectIDConverter

    return app

