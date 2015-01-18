from common.models import UserModel
from common.models import ProjectModel
import flask as fk
from smt_view import app


@app.route('/user/view/<objectid:id>')
def user_view(id):
    user = UserModel.objects.with_id(id)
    projects = ProjectModel.objects(user=user)
    return fk.render_template('user.html', user=user, projects=projects)
