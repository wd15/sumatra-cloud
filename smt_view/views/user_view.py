from common.models import UserModel
import flask as fk
from smt_view import app


@app.route('/user/view/<objectid:id>')
def user_view(id):
    user = UserModel.objects.with_id(id)
    data, columns = user.get_datatable()
    return fk.render_template('user.html', user=user, data=data, columns=columns)


