from .. import db
from ..models import UserModel
#from ..models import RecordModel


class ProjectModel(db.Document):
    user = db.ReferenceField(UserModel, reverse_delete_rule=db.CASCADE)
    name = db.StringField(max_length=300, required=True)


