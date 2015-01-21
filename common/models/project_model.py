from ..core import db
from ..models import UserModel
import json
import datetime


class ProjectModel(db.Document):
    user = db.ReferenceField(UserModel, reverse_delete_rule=db.CASCADE, required=True)
    name = db.StringField(max_length=300, required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now)
    
    def to_smt_json(self, request):
        from ..models import RecordModel
        query = RecordModel.objects(project=self)
        records = [r.to_json() for r in query]
        return json.dumps({'project' : self.name, 'url' : request.url, 'records' : records})

    def _count(self):
        from ..models import RecordModel
        return RecordModel.objects(project=self).count()

