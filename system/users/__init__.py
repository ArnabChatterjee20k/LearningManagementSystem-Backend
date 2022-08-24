from flask import Blueprint
from flask_restful import Api

user = Blueprint("user",__name__)
api = Api(user)
from system.users.Register import Register
from system.users.Login import Login
api.add_resource(Register,"/register")
api.add_resource(Login,"/login")