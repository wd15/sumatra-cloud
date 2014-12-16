from app import app
import flask as fk
import json
from ..models import ProjectModel
from ..models import UserModel
from flask.ext.api import status

API_VERSION = 3

api_url = '/api/v{0}'.format(API_VERSION)

@app.route(api_url)
def api():
    return 'api'

@app.route(api_url + '/<project_name>/', methods=['GET', 'PUT'])
def project(project_name):
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
    
@app.route(api_url + '/<project_name>/tag/<tag>/')
def api_project_tag(project_name, tag):
    return 'api_project_tag'
# @app.route(api_url + '/client-test/<stuff>', )
# def client_test(stuff):
#     return 'client_test'

                       
