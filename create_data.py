from app import db, models

users = (models.User(name='Daniel Wheeler', email='daniel.wheeler2@gmail.com'),
         models.User(name='Susan James', email='susan.james@gmail.com'))

for u in users:
    db.session.add(u) 
db.session.commit()

projects = (models.Project(name='extremefill', user=users[0]),
            models.Project(name='superfill', user=users[0]),
            models.Project(name='phasefield', user=users[1]))

for p in projects:
    db.session.add(p)
db.session.commit()

                           
