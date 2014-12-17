from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import jinja2
from flask import url_for, get_flashed_messages
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
app.debug = True
db = SQLAlchemy(app)

loader = jinja2.PackageLoader('app', 'templates')
template_env = jinja2.Environment(autoescape=True, loader=loader)
template_env.globals.update(url_for=url_for)
template_env.globals.update(get_flashed_messages=get_flashed_messages)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_view'
openid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
