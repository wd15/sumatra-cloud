from app import db, models

print db.session.query(models.UserModel).all()
db.session.query(models.UserModel).delete()
print db.session.query(models.ProjectModel).all()
db.session.query(models.ProjectModel).delete()

db.session.commit()

                           
