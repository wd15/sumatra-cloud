from ..core import db
from ..models import ProjectModel
import json

class RecordHeadModel(db.Document):
    project = db.ReferenceField(ProjectModel, reverse_delete_rule=db.CASCADE)
    label = db.StringField(max_length=300)
    timestamp = db.StringField(max_length=50)
    duration = db.IntField(default=0)
    reason = db.StringField(max_length=300)
    outcome = db.StringField(max_length=300)
    #-1,0,1,2,3 for Crashed, Unknown, Started, Running, Finished
    status = db.IntField(min_value=-1, max_value=3, default=0)
    def to_smt_json(self):
        return json.dumps({'label':self.label, 'status':self.status, 'timestamp':self.timestamp, 'duration':self.duration, 'reason':self.reason, 'outcome':self.outcome})

class RecordModel(db.Document):
    head = db.ReferenceField(RecordHeadModel, reverse_delete_rule=db.CASCADE)
    data = db.DictField()

    def to_smt_json(self):
        return json.dumps({'label':self.head.label, 'status':self.head.status, 'timestamp':self.head.timestamp, 'duration':self.head.duration, 'reason':self.head.reason, 'outcome':self.head.outcome, 'data':self.data})

        

