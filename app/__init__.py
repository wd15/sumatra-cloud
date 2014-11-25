from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import jinja2
from jinja2 import Environment, PackageLoader
import os
from flask import url_for, get_flashed_messages

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

# templates
# path_to_templates = os.path.join(os.path.dirname(__file__), '..', 'templates')
# loader = jinja2.FileSystemLoader(path_to_templates)
loader = jinja2.PackageLoader('app', 'templates')
template_env = jinja2.Environment(autoescape=True, loader=loader)
template_env.globals.update(url_for=url_for)
template_env.globals.update(get_flashed_messages=get_flashed_messages)

