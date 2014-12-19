from app import app
import flask as fk
import login_view
import user_view
# import api_view

@app.route('/')
@app.route('/index')
def index_view():
    return fk.render_template('index.html')

@app.route('/learn')
def learn_view():
    return fk.redirect(fk.url_for('index_view'))



