from app import app
import jinja2
import os
from flask import url_for


# templates
loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
env = jinja2.Environment(autoescape=True,
                         loader=loader)
env.globals.update(url_for=url_for)
project_html = env.get_template('project.html')
front_html = env.get_template('front.html')

@app.route('/')
def front_view():
    return front_html.render()

@app.route('/project')
def project_view():
    return project_html.render()

# def login_view():
#     pass

# @app.route('/<user>/<project>')
# def project_view(user, project):
#     pass

# @app.route('/<user>/<project>/<record>')
# def record_view(user, project, record):
#     pass

