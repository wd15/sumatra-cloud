from .. import db

class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    projects = db.relationship('ProjectModel', backref='user', lazy='dynamic')
    
    def __repr__(self):
        return '<User %r>' % (self.nickname)

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

    @classmethod
    def get_by_id(cls, id):
        return db.session.query(cls).get(id)

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_nickname(cls, name):
        return db.session.query(cls).filter_by(nickname=name).first()

    @classmethod
    def get_anonymous(cls):
        name = 'anonymous'
        user = cls.get_by_nickname(name)
        if user is None:
            user = cls(email='', nickname=name)
            user.add()
        return user

