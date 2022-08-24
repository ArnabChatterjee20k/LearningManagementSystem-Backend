from flask_restful import Resource, abort
from flask import request
from system.users.Parser import UserDataParser, ValidityCheckerParser
from system.utils.JWT import generate_payload, verify_payload
from system.Models.User import User
from system import db
from system.utils.Mail import sendmail
from system.utils.TimeTokens import serialise_token, deserialise_token
from flask_mail import Message


class Register(Resource):
    user_data = UserDataParser()
    email_data = ValidityCheckerParser()

    @user_data.validate
    def post(self, data):
        # we will need token from the request query string
        # first send request to the get endpoint then take the token then post here and create account
        validtoken = data.get("token")
        try:
            email = deserialise_token(validtoken) # json string and if we use get here then it will give error as get cant be used on str
            token = generate_payload(email) # passing the json email object itself
            user = User()
            user.name = data.get("name")
            user.password = data.get("password")
            user.email = email.get("email")
            try:
                db.session.add(user)
                db.session.commit()
            except:
                return abort(500)
            return {"token": token, "status": "success"}, 200
        except Exception as e:
            print(e)
            return {"token": "expired"}, 400

    @email_data.validate
    def get(self, data):
        email = data.get("email")
        kwargs = {"email": email}
        token = serialise_token(**kwargs)
        url = request.base_url+f"""token={token}"""
        message = f"""We got a registration request from your account.
Plz follow the below link to create your account which is valid for 1 hour
{url}
"""
        sendmail.delay("LMS", message, email)
        ## We will not be sending token in the response token will be send in the email
        ## It is just for confirmation
        return {"validity token": token, "status": "success", "registration-endpoint": url}, 200