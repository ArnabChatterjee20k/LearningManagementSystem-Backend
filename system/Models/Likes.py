from system import db
class Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer,db.ForeignKey("user.id",onupdate="CASCADE", ondelete="CASCADE"),nullable=False)
    video = db.Column(db.Integer,db.ForeignKey("video.id",onupdate="CASCADE", ondelete="CASCADE"),nullable=False)
