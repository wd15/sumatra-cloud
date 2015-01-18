import json

from flask.ext.api import status
import flask as fk

from smt_api import app
from common.models import ProjectModel
from common.models import RecordModel
from common.tools.basic_auth import requires_auth


API_VERSION = 3

API_URL = '/api/v{0}'.format(API_VERSION)

@app.route(API_URL + '/<project_name>/', methods=['GET', 'PUT', 'DELETE'])
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
    elif fk.request.method == 'DELETE':
        project = ProjectModel.objects(name=project_name, user=fk.g.user).first_or_404()
        project.delete()
        return fk.Response('Project deleted', status.HTTP_200_OK)


@app.route(API_URL + '/<project_name>/<record_label>/', methods=['GET', 'DELETE'])
@requires_auth
def record(project_name, record_label):
    project = ProjectModel.objects(name=project_name, user=fk.g.user).first_or_404()
    if fk.request.method == 'GET':
        recordHead = RecordModel.objects(project=project, label=record_label).first_or_404()
        return fk.Response(recordHead.to_json(), mimetype='application/json')
    elif fk.request.method == 'PUT':
        data = json.loads(fk.request.data)
        record, created = RecordModel.objects.get_or_create(project=project, label=record_label)
        recordHead.update(data)
    elif fk.request.method == 'DELETE':
        record = RecordModel.objects(project=project, label=record_label).first_or_404()
        record.delete()
        return fk.Response('Record deleted', status.HTTP_200_OK)

