from flask import Blueprint
from flask_restful import Api
from system.admin.resource import Admin

admin = Blueprint("admin",__name__)
api = Api(admin)
api.add_resource(Admin,"/")