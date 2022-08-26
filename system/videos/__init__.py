from flask_restful import Api
from flask import Blueprint
from system.videos.AllVideos import AllVideos

videos = Blueprint("videos",__name__)
api = Api(videos)
api.add_resource(AllVideos,"/")