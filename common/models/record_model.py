from ..core import db
from ..models import ProjectModel

class RecordModel(db.Document):
    project = db.ReferenceField(ProjectModel, reverse_delete_rule=db.CASCADE)
    label = db.StringField(max_length=300)
    data = db.DictField()

