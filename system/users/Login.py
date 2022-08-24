from flask_restful import Resource , abort
from system.Models.User import User
from system.users.Parser import LoginParser
from system.utils.JWT import generate_payload

class Login(Resource):
    # we dont need token here as we are logging to get the token
    parser = LoginParser()
    @parser.validate
    def post(self,data):
        try:
            email = data.get("email")
            password = data.get("password")
            user = User.query.filter_by(email=email).first_or_404()
            if not User.check_password(user.password,password):
                return {"status":"invalid password"},400
            token = generate_payload({"email":email})
            return {"token":token,"status":"success"},200
        except Exception as e:
            print(e)
            return {"status":"invalid authentication"},400
        