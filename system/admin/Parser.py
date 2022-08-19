from flask import abort
import secrets
from flask_restful import reqparse , inputs
from functools import wraps
from system.admin.JWT import verify_payload
from jwt import decode
class VideoParser:
    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parsing_location = "json"
        
        self.parser.add_argument("title",type=str,required=True,location=self.parsing_location)
        self.parser.add_argument("description",type=str,required=True,location=self.parsing_location)
        self.parser.add_argument("link",type=str,help="plz provide a valid link",required=True,location=self.parsing_location)

    def validate(self,function_to_be_validated):
        try:
            @wraps(function_to_be_validated)
            def check(*args,**kwargs):
                data = self.parser.parse_args()
                print(data)
                return function_to_be_validated(*args,**kwargs)
            return check
        except Exception as e:
            return(e)

class LoginParser:
    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parsing_location = "headers"
        self.parser.add_argument("access-token",type=str,required=True,location=self.parsing_location)
    
    def validate(self,function_to_be_validated):
        try:
            @wraps(function_to_be_validated)
            def check(*args,**kwargs):
                data = self.parser.parse_args()
                try:
                    token = verify_payload(data.get("access-token"))
                    print(token)
                    return function_to_be_validated(token,*args,**kwargs)
                except:
                    return {"message":"invalid token"},400
            return check
        except Exception as e:
            print(e)
            return {"status":"internal server error"},500