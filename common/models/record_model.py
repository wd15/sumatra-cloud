from ..core import db
from ..models import ProjectModel
import json

class RecordModel(db.Document):
    project = db.ReferenceField(ProjectModel, reverse_delete_rule=db.CASCADE, required=True)
    label = db.StringField(max_length=300, required=True)
    data = db.DictField()

    def to_smt_json(self):
        return json.dumps(self.data)

        

