import jwt
from functools import wraps
from flask import current_app , request , abort

def generate_payload(data):
    secret = current_app.config["SECRET_KEY"]
    return jwt.encode(data,secret)

def verify_payload(token):
    secret = current_app.config["SECRET_KEY"]
    return jwt.decode(token,secret,algorithms=["HS256"])

def tokenrequired(function):
    @wraps(function)
    def check(*args,**kwargs):
        token = request.headers.get("access-token")
        if not token:
            return {"status":"token not found"},400
        try:
            data = verify_payload(token)
            print(data)
            return function(data,*args,**kwargs)
        except:
            return {"status":"invalid token"},400
    return check
