from src.app import db


class Bug(db.Model):
    __tablename__ = 'testcases_bug'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bug_id = db.Column(db.Integer)
    summary = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    case_id = db.Column(db.Integer, nullable=True)
    case_run_id = db.Column(db.Integer, nullable=True)
    bug_system_id = db.Column(db.Integer)
    creation_date = db.Column(db.DateTime, nullable=True)

    def keys(self):
        return ['id', 'bug_id', 'summary', 'description', 'case_id', 'case_run_id', 'bug_system_id', 'creation_date']

    def __getitem__(self, item):
        return getattr(self, item)

    def get_data(self):
        return {
            'id': self.id,
            'bug_id': self.bug_id,
            'summary': self.summary,
            'description': self.description,
            'case_id': self.case_id,
            'case_run_id': self.case_run_id,
            'bug_system_id': self.bug_system_id,
            'creation_date': self.creation_date.strftime('%Y/%m/%d %H:%M:%S') if self.creation_date else ''
        }
