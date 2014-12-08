from app import app, oid, lm, db
from flask import url_for, redirect, render_template, g, session, flash, request
from flask.ext.login import login_user, current_user, login_required, logout_user

from ..forms import LoginForm
from ..models import UserModel

@app.route('/')
@app.route('/index')
def index_view():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login_view():
    # import pdb; pdb.set_trace()
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('user_view', user=g.user.nickname))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@lm.user_loader
def load_user(id):
    return UserModel.query.get(int(id))

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login_view'))
    user = UserModel.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = UserModel(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.before_request
def before_request():
    g.user = current_user

@login_required
@app.route('/<user>')
def user_view(user):
    return render_template('user.html')

@app.route('/learn')
def learn_view():
    return redirect(url_for('index_view'))

@app.route('/logout')
def logout_view():
    logout_user()
    return redirect(url_for('index_view'))
