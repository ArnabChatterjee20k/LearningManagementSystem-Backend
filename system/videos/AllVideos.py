from flask_restful import Resource , marshal , fields
from system.Models.Video import Video
class AllVideos(Resource):
    def get(self):
        return marshal(Video.query.all(),fields.List)