from flask import Blueprint
from flask_restful import Api

user = Blueprint("user",__name__)
api = Api(user)
from system.users.Register import Register
api.add_resource(Register,"/user/register")