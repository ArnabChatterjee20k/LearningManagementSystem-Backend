from system import db
from werkzeug.security import generate_password_hash , check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(30))
    _password = db.Column(db.Integer)
    videos = db.relationship("Video",lazy="dynamic",backref = "creator")
    playlist = db.relationship("Playlist",lazy="dynamic",backref = "playlist")
    liked_videos = db.relationship("Likes",lazy="dynamic",backref = "liked_videos")

    ## we will be using password instead of _password to get the data. Made a getter then a setter
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,hashed_password):
        self._password = generate_password_hash(hashed_password)

    @classmethod
    def check_password(cls,password_hash,password):
        return check_password_hash(password_hash,password)
