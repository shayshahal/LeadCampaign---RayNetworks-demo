from . import db


class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.String(), nullable=False)
    fieldData = db.Column(db.String(), nullable=False)

    def __init__(self, id, created_time, fieldData):
        self.id = id
        self.created_time = created_time
        self.fieldData = ','.join('{0}: {1}'.format(
            obj['name'], obj['values']) for obj in fieldData)

    def __repr__(self):
        return 'lead: ' + self.created_time
