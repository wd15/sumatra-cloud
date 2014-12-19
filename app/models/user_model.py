from app import db
import datetime

class UserModel(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    email = db.StringField(max_length=120, required=True, unique=True)
    nickname = db.StringField(max_length=64, required=True)

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
    def get_anonymous(cls):
        name = 'anonymous'
        user = cls.query.filter_by(nickname=name).first()
        if user is None:
            user = cls(email='', nickname=name)
            user.add()
        return user

