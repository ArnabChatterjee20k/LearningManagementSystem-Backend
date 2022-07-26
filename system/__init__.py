from flask import Flask
from system.Config import Config

# We will import Resources , Api where we define them
# Here in this init file we will just register the blueprints

def create_api():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app