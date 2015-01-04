from ..core import db
from ..models import UserModel
import json


class ProjectModel(db.Document):
    user = db.ReferenceField(UserModel, reverse_delete_rule=db.CASCADE, required=True)
    name = db.StringField(max_length=300, required=True)

    def to_smt_json(self, request):
        from ..models import RecordModel
        record_query = RecordModel.objects(project=self)
        record_urls = [request.url + r.label for r in record_query]
        project_dict = dict()
        project_dict['records'] = record_urls        
        return json.dumps(project_dict)


