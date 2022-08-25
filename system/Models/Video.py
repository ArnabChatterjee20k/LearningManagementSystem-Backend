from system import db
from datetime import datetime
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),nullable = False)
    description = db.Column(db.Text,nullable=False)
    created_on = db.Column(db.DateTime, default = datetime.now())
    author = db.Column(db.Integer,db.ForeignKey("user.id",onupdate="CASCADE", ondelete="CASCADE"),nullable=False)
