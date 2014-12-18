from app import app
from ..models import UserModel
import flask as fk

@app.route('/user/view/<int:id>')
def user_view(id):
    user = UserModel.query.get(id)
    return fk.render_template('user.html', user=user)
