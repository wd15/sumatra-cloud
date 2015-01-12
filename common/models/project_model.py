from ..core import db
from ..models import UserModel
import json
import datetime


class ProjectModel(db.Document):
    user = db.ReferenceField(UserModel, reverse_delete_rule=db.CASCADE, required=True)
    name = db.StringField(max_length=300, required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now)
    
    def to_smt_json(self, request):
        from ..models import RecordModel
        record_query = RecordModel.objects(project=self)
        record_urls = [request.url + r.label for r in record_query]
        project_dict = dict()
        project_dict['records'] = record_urls        
        return json.dumps(project_dict)

    def _count(self):
        from ..models import RecordModel
        return RecordModel.objects(project=self).count()

    def get_datatable(self):
        from ..models import RecordModel
        records = RecordModel.objects(project=self)
        data = [[r.label,
                 r.data["duration"],
                 r.data["executable"]["name"],
                 r.data["version"][:12],
                 r.data["tags"],
                 r.data["main_file"],
                 r.project.user.email,
                 r.data["timestamp"]] for r in records]
        titles = ["Label", "Duration", "Executable", "Version", "Tags", "Main File", "Email", "Time Stamp"]
        columns = [{"title" : t} for t in titles]
        return data, columns

