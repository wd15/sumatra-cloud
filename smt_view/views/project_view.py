import flask as fk
from smt_view import app
from common.models import ProjectModel

@app.route('/project/view/<objectid:id>')
def project_view(id):
    project = ProjectModel.objects.with_id(id)
    data, columns = project.get_datatable()
    return fk.render_template('user.html', user=project.user, data=data, columns=columns)
