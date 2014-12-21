from flask import Flask
import jinja2
from flask import url_for, get_flashed_messages
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir
from flask.ext.mongoengine import MongoEngine
import tools

app = Flask(__name__)
app.config.from_object('config')
app.debug = True

## templates

loader = jinja2.PackageLoader('app', 'templates')
template_env = jinja2.Environment(autoescape=True, loader=loader)
template_env.globals.update(url_for=url_for)
template_env.globals.update(get_flashed_messages=get_flashed_messages)

## login mangager

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_view'
openid = OpenID(app, os.path.join(basedir, 'tmp'))

## Flask-MongoEngine

db = MongoEngine(app)

## Custom Converters

app.url_map.converters['objectid'] = tools.ObjectIDConverter

## Required imports to make app work

from app import views, models
