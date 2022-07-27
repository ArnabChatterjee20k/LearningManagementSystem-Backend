from flask_restful import Resource , marshal_with , fields
from flask import request
from validator import validate
rules = {
    "video_name":"required|min:10",
    "video_desp":"required|max:1"
}
class Admin(Resource):
    def post(self):
        result, _, errors = validate(request.get_json(force=True), rules, return_info=True)
        return [result,errors]