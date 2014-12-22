# The app module
from flask import Flask
import jinja2
from flask import url_for, get_flashed_messages
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir
from common.core import app

# Templates
loader = jinja2.PackageLoader('app', 'templates')
template_env = jinja2.Environment(autoescape=True, loader=loader)
template_env.globals.update(url_for=url_for)
template_env.globals.update(get_flashed_messages=get_flashed_messages)

# Login mangager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_view'
openid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views
from common import models
