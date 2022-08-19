from flask_restful import reqparse , inputs
from functools import wraps
class VideoParser:
    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parsing_location = "json"
        
        self.parser.add_argument("title",type=str,required=True,location=self.parsing_location)
        self.parser.add_argument("description",type=str,required=True,location=self.parsing_location)
        self.parser.add_argument("link",type=inputs.regex(("/$[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi^")),help="plz provide a valid link",required=True,location=self.parsing_location)

    def validate(self,function_to_be_validated):
        try:
            @wraps(function_to_be_validated)
            def check(*args,**kwargs):
                self.parser.parse_args()
                return function_to_be_validated(*args,**kwargs)
            return check
        except Exception as e:
            return(e)
