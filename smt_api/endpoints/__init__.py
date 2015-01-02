from smt_api import app
import flask as fk
import json

from common.models import ProjectModel
from common.models import UserModel
from common.models import RecordModel
from flask.ext.api import status

API_VERSION = 3

url = '/api/v{0}'.format(API_VERSION)

@app.route(url + '/<project_name>/', methods=['GET', 'PUT'])
def project(project_name):
    user = UserModel.get_anonymous()
    if fk.request.method == 'PUT':
        project, created = ProjectModel.objects.get_or_create(name=project_name, user=user)
        if created:
            return fk.make_response('Created project', status.HTTP_201_CREATED)
        else:
            return fk.make_response('Project already exists', status.HTTP_200_OK)
    elif fk.request.method == 'GET':
        project = ProjectModel.objects(name=project_name, user=user).first_or_404()
        return fk.Response(project.to_json(), mimetype='application/json')

@app.route(url + '/<project_name>/<record_label>/', methods=['GET', 'PUT'])
def record(project_name, record_label):
    user = UserModel.get_anonymous()
    project = ProjectModel.objects(name=project_name, user=user).first_or_404()
    if fk.request.method == 'PUT':
        data_dict = json.loads(fk.request.data)
        record, created = RecordModel.objects.get_or_create(label=record_label, project=project, data=data_dict)
        if created:
            return fk.make_response('Record added to project', status.HTTP_201_CREATED)
        else:
            return fk.make_response('Record already exists', status.HTTP_409_CONFLICT)
    elif fk.request.method == 'GET':
        record = RecordModel.objects(project=project, label=record_label).first_or_404()
        return fk.Response(record.to_json(), mimetype='application/json')
    
@app.route(url + '/<project_name>/tag/<tag>/')
def project_tag(project_name, tag):
    return 'api_project_tag'
# @app.route(api_url + '/client-test/<stuff>', )
# def client_test(stuff):
#     return 'client_test'

                       

