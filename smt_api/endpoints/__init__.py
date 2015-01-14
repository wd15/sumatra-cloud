import json

from flask.ext.api import status
import flask as fk

from smt_api import app
from common.models import ProjectModel
from common.models import UserModel
from common.models import RecordModel, RecordHeadModel
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


@app.route(API_URL + '/<project_name>/<record_label>/view/', methods=['GET', 'DELETE'])
@requires_auth
def view_record(project_name, record_label):
    project = ProjectModel.objects(name=project_name, user=fk.g.user).first_or_404()
    if fk.request.method == 'GET':
        recordHead = RecordHeadModel.objects(project=project, label=record_label).first_or_404()
        record = RecordModel.objects(head=recordHead).first_or_404()
        return fk.Response(record.to_smt_json(), mimetype='application/json')
    elif fk.request.method == 'DELETE':
        head = RecordHeadModel.objects(project=project, label=record_label).first_or_404()
        head.delete()
        return fk.Response('Record deleted', status.HTTP_200_OK)
 
@app.route(API_URL + '/<project_name>/<record_label>/begin/', methods=['PUT'])
@requires_auth
def begin_record(project_name, record_label):
    project = ProjectModel.objects(name=project_name, user=fk.g.user).first_or_404()
    if fk.request.method == 'PUT':
        head_dict = json.loads(fk.request.data)
        recordHead, createdHead = RecordHeadModel.objects.get_or_create(label=record_label, project=project)
        record, createdBody = RecordModel.objects.get_or_create(head=recordHead, data={})
        recordHead.timestamp = head_dict["timestamp"]
        recordHead.duration = head_dict["duration"]
        recordHead.reason = head_dict["reason"]
        recordHead.outcome = head_dict["outcome"]
        recordHead.status = 0
        recordHead.save()
        return fk.make_response('Record initiated in the project.', status.HTTP_201_CREATED)

@app.route(API_URL + '/<project_name>/<record_label>/finish/', methods=['PUT'])
@requires_auth
def finish_record(project_name, record_label):
    project = ProjectModel.objects(name=project_name, user=fk.g.user).first_or_404()
    if fk.request.method == 'PUT':
        data_dict = json.loads(fk.request.data)
        recordHead = RecordHeadModel.objects(project=project, label=record_label).first_or_404()
        record = RecordModel.objects(head=recordHead).first_or_404()
        record.data = data_dict
        record.save()
        return fk.make_response('Record finished in the project.', status.HTTP_200_OK)

@app.route(API_URL + '/<project_name>/<record_label>/status/', methods=['PUT', 'GET'])
@requires_auth
def status_record(project_name, record_label):
    project = ProjectModel.objects(name=project_name, user=fk.g.user).first_or_404()
    if fk.request.method == 'PUT':
        data = json.loads(fk.request.data)
        head = RecordHeadModel.objects(project=project, label=record_label).first_or_404()
        head.status = data["status"]
        head.save()
        return fk.Response('Record status updated', status.HTTP_200_OK)
    elif fk.request.method == 'GET':
        head = RecordHeadModel.objects(project=project, label=record_label).first_or_404()
        if head.status == -1:
            return fk.Response('Failed', status.HTTP_200_OK)
        elif head.status == 0:
            return fk.Response('Unknown', status.HTTP_200_OK)
        elif head.status == 1:
            return fk.Response('Started', status.HTTP_200_OK)
        elif head.status == 2:
            return fk.Response('Running', status.HTTP_200_OK)
        elif head.status == 3:
            return fk.Response('Finished', status.HTTP_200_OK)
        else:
            return fk.Response('Undefinied', status.HTTP_200_OK)
