from flask import Blueprint
from flask_restful import Api
from system.admin.AdminVideos import AdminVideos
from system.admin.AdminAuth import AdminLogin
# since admin is just like an instance of flask app so we can use it as blueprint
admin = Blueprint("admin",__name__)
api = Api(admin)

api.add_resource(AdminVideos,"/")
api.add_resource(AdminLogin,"/admin/login")