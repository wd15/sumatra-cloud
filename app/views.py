from app import app
import jinja2
import os
from flask import url_for, redirect, flash, get_flashed_messages

from .forms import Login


# templates
loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
env = jinja2.Environment(autoescape=True,
                         loader=loader)
env.globals.update(url_for=url_for)
env.globals.update(get_flashed_messages=get_flashed_messages)
project_html = env.get_template('project.html')
front_html = env.get_template('front.html')

@app.route('/', methods=['GET', 'POST'])
def front_view():
    form = Login()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
        (form.openid.data, str(form.remember_me.data)))
        return redirect(url_for('project_view'))
    else:
        return front_html.render(form=form)

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

