from .. import db

class RecordModel(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    label = db.Column(db.String(300))

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    @property
    def serialize(self):
        return {'id': self.id,
                'project_id': self.project_id,
                'label': self.label}
