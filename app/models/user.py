from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    project = db.relationship('Project', backref='user', lazy='dynamic')
    name = db.Column(db.String(300))
    
    def __repr__(self):
        return '<User %r>' % (self.nickname)

    
