from .. import db

class ProjectModel(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(300))
    description = db.Column(db.Text())

    @property
    def serialize(self):
        return {'id': self.id,
                'name': self.name,
                'description': self.description,
                'records': [],
                'access': [],
                'tags': []}

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_name(cls, name):
        return db.session.query(cls).filter_by(name=name).first()

