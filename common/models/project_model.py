from ..core import db
from ..models import UserModel
import json


class ProjectModel(db.Document):
    user = db.ReferenceField(UserModel, reverse_delete_rule=db.CASCADE, required=True)
    name = db.StringField(max_length=300, required=True)

    def to_smt_json(self, request):
        from ..models import RecordHeadModel
        head_query = RecordHeadModel.objects(project=self)
        heads = [r.to_smt_json() for r in head_query]
        return json.dumps({'project':self.name, 'url':request.url, 'records': heads})


