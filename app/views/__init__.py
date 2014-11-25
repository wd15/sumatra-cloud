from app import app
from flask import url_for, redirect, flash, render_template
from ..forms import LoginForm

@app.route('/')
@app.route('/index')
def index_view():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login_view():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
        (form.openid.data, str(form.remember_me.data)))
        return redirect(url_for('project_view'))
    else:
        return render_template('login.html', form=form)

@app.route('/project')
def project_view():
    return render_template('project.html')

