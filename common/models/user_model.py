import datetime
from ..core import db
import json
import flask as fk

class UserModel(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now)
    email = db.StringField(max_length=120, required=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.email)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def to_table_json(self):
        from common.models import ProjectModel
        projects = ProjectModel.objects(user=self)
        data = [[p.name,
                 p.user.email,
                 p._count(),
                 p.created_at.strftime('%x %X'),
                 fk.url_for('project_view', id=p.id)] for p in projects]
        return json.dumps(data)
        
        
