from flask_restful import Resource , abort
from system.users.Parser import UserDataParser
from system.utils.JWT import generate_payload
class Register(Resource):
    parser = UserDataParser()
    @parser.validate
    def post(self,data):
        try:
            token = generate_payload({"email":data.get("email")})
            return {token:token,"status":"success"},200
        except:
            return abort(500)