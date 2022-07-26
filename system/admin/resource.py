from flask import Blueprint
from flask_restful import Resource , Api

admin = Blueprint("admin",__name__)

class Admin(Resource):
    def get(self):
        return "Hellwo"

# using blueprint instead of Flask instance
api = Api(admin)
api.add_resource(Admin,"/")