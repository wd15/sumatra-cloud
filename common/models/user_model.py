import datetime
from ..core import db
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

    def get_datatable(self):
        from common.models import ProjectModel
        projects = ProjectModel.objects(user=self)
        data = [['<a href="{0}">{1}</a>'.format(fk.url_for('project_view', id=p.id), p.name),
                 p.user.email,
                 p._count(),
                 p.created_at.strftime('%x %X')] for p in projects]
        titles = ["Name", "User", "Number of Records", "Created"]
        columns = [{"title" : t} for t in titles]
        return data, columns
        
        
