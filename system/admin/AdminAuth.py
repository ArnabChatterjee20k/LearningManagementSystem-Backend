from flask_restful import Resource
from system.admin.Parser import LoginParser
class AdminLogin(Resource):
    Login = LoginParser()
    @Login.validate
    def get(self,*args,**kwargs):
        print(args)
        return "done"