from system import db
from datetime import datetime
class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, default = datetime.now())
    author = db.Column(db.Integer,db.ForeignKey("user.id",onupdate="CASCADE", ondelete="CASCADE"),nullable=False)
    video = db.Column(db.Integer,db.ForeignKey("video.id",onupdate="CASCADE", ondelete="CASCADE"),nullable=False)


