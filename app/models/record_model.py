from .. import db
from ..models import ProjectModel

class RecordModel(db.Document):
    project = db.ReferenceField(ProjectModel, reverse_delete_rule=db.CASCADE)
    label = db.StringField(max_length=300)

    @property
    def serialize(self):
        return {'id': self.id,
                'project_id': self.project.id,
                'label': self.label}

## add class RecordHead
