from .. import db
from ..models import UserModel
#from ..models import RecordModel


class ProjectModel(db.Document):
    user = db.ReferenceField(UserModel, reverse_delete_rule=db.CASCADE)
    name = db.StringField(max_length=300, required=True)
    #    records = db.ListField(db.EmbeddedDocumentField(RecordModel))

    @property
    def serialize(self):
        return {'id': str(self.id),
                'name': self.name,
                'description': '',
                'records': [],
                'access': [],
                'tags': []}




