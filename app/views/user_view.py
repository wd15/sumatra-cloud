from app import app
from ..models import UserModel
import flask as fk


@app.route('/user/view/<objectid:id>')
def user_view(id):
    user = UserModel.objects.with_id(id)
    return fk.render_template('user.html', user=user)
