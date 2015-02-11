# The app module
# from flask import Flask
import jinja2
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
import flask as fk
from config import basedir
from common.core import setup_app

app = setup_app(__name__)

# Templates
loader = jinja2.PackageLoader('smt_view', 'templates')
template_env = jinja2.Environment(autoescape=True, loader=loader)
template_env.globals.update(url_for=fk.url_for)
template_env.globals.update(get_flashed_messages=fk.get_flashed_messages)

# Login mangager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_view'
openid = OpenID(app, os.path.join(basedir, 'tmp'))

from . import views
from common import models
from . import filters
