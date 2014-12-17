from app import app
import flask as fk

from ..models import ProjectModel
from ..models import UserModel
from ..models import RecordModel
from flask.ext.api import status

API_VERSION = 3

api_url = '/api/v{0}'.format(API_VERSION)

@app.route(api_url)
def api():
    return 'api'

@app.route(api_url + '/<project_name>/', methods=['GET', 'PUT'])
def project_api(project_name):
    if fk.request.method == 'PUT':
        project = ProjectModel.query.filter_by(name=project_name).first()
        if project:
            return fk.make_response('Project already exists', status.HTTP_200_OK)
        else:
            user = UserModel.get_anonymous()
            project = ProjectModel(user=user, name=project_name)
            project.add()
            return fk.make_response('Created project', status.HTTP_201_CREATED)
    elif fk.request.method == 'GET':
        project = ProjectModel.query.filter_by(name=project_name).first_or_404()
        return fk.json.jsonify(project.serialize)

@app.route(api_url + '/<project_name>/<record_label>/', methods=['GET', 'PUT'])
def record_api(project_name, record_label):
    project = ProjectModel.query.filter_by(name=project_name).first_or_404()
    record = RecordModel.query.filter_by(label=record_label).first()
    if fk.request.method == 'PUT':
        if record is None:
            record = RecordModel(project=project, label=record_label)
            record.add()
            return fk.make_response('Record added to project', status.HTTP_201_CREATED)
        else:
            return fk.make_response('Record already exists', status.HTTP_409_CONFLICT)
    elif fk.request.method == 'GET':
        if record is None or project.id != record.project_id:
            return fk.make_response('Record not found', status.HTTP_404_NOT_FOUND)
        else:
            return fk.json.jsonify(record.serialize)
    
@app.route(api_url + '/<project_name>/tag/<tag>/')
def api_project_tag(project_name, tag):
    return 'api_project_tag'
# @app.route(api_url + '/client-test/<stuff>', )
# def client_test(stuff):
#     return 'client_test'

                       
