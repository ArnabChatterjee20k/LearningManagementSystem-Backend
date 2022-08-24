from functools import wraps
from flask_restful import reqparse , inputs , abort

def validate_wrapper_function(self,function):
        try:
            @wraps(function)
            def check(*args,**kwargs):
                data = data = self.parser.parse_args()
                return function(data=data,*args,**kwargs)
            return check
        except:
            return abort(500)

class UserDataParser:
    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parsing_location = "json"
        self.query_location="args"
        self.parser.add_argument("name",type=str,required=True,location=self.parsing_location)
        self.parser.add_argument("token",required=True,location=self.query_location)
        self.parser.add_argument("password",type=str,required=True,location=self.parsing_location)

    def validate(self,function):
        return validate_wrapper_function(self,function)

class ValidityCheckerParser:
    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.query_location="args"
        self.parser.add_argument("email",type=inputs.regex("^([_\-\.a-zA-Z0-9]+)@([_\-\.a-zA-Z0-9]+)\.([a-zA-Z]){2,5}$"),help="Not a valid email",required=True,location=self.query_location)

    def validate(self,function):
        return validate_wrapper_function(self,function)

class LoginParser:
    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parsing_location="json"
        self.parser.add_argument("email",type=inputs.regex("^([_\-\.a-zA-Z0-9]+)@([_\-\.a-zA-Z0-9]+)\.([a-zA-Z]){2,5}$"),help="Not a valid email",required=True,location=self.parsing_location)
        self.parser.add_argument("password",type=str,required=True,location=self.parsing_location)

    def validate(self,function):
        return validate_wrapper_function(self,function)