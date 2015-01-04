import json

from flask.ext.api import status
import flask as fk

from smt_api import app
from common.models import ProjectModel
from common.models import UserModel
from common.models import RecordModel
from common.tools.basic_auth import requires_auth


API_VERSION = 3

API_URL = '/api/v{0}'.format(API_VERSION)

@app.route(API_URL + '/<project_name>/', methods=['GET', 'PUT'])
@requires_auth
def project(project_name):
    if fk.request.method == 'PUT':
        project, created = ProjectModel.objects.get_or_create(name=project_name, user=fk.g.user)
        if created:
            return fk.make_response('Created project', status.HTTP_201_CREATED)
        else:
            return fk.make_response('Project already exists', status.HTTP_200_OK)
    elif fk.request.method == 'GET':
        project = ProjectModel.objects(name=project_name, user=fk.g.user).first_or_404()
        return fk.Response(project.to_smt_json(fk.request), mimetype='application/json')

@app.route(API_URL + '/<project_name>/<record_label>/', methods=['GET', 'PUT'])
@requires_auth
def record(project_name, record_label):
    project = ProjectModel.objects(name=project_name, user=fk.g.user).first_or_404()
    if fk.request.method == 'PUT':
        data_dict = json.loads(fk.request.data)
        record, created = RecordModel.objects.get_or_create(label=record_label, project=project, data=data_dict)
        if created:
            return fk.make_response('Record added to project', status.HTTP_201_CREATED)
        else:
            return fk.make_response('Record already exists', status.HTTP_409_CONFLICT)
    elif fk.request.method == 'GET':
        record = RecordModel.objects(project=project, label=record_label).first_or_404()
        return fk.Response(record.to_smt_json(), mimetype='application/json')
    





                       

