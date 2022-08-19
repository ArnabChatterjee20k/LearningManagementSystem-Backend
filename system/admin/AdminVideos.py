from flask_restful import Resource 
from system.admin.Parser import VideoParser

class AdminVideos(Resource):
    Parser = VideoParser()
    @Parser.validate
    def post(self):
        try:
            return "done"
        except Exception as e:
            print(e)
            return e