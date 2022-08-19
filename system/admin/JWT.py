import jwt
from functools import wraps
from flask import current_app

def generate_payload(data):
    secret = current_app.config["SECRET_KEY"]
    return jwt.encode(data,secret)

def verify_payload(token):
    secret = current_app.config["SECRET_KEY"]
    return jwt.decode(token,secret,algorithms=["HS256"])