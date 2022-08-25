import os
from flask import Flask
from system.Config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from celery import Celery

db = SQLAlchemy()
mail = Mail()
migrate = Migrate(render_as_batch=True)

celery = Celery(__name__,broker=Config.broker_url, result_backend=Config.result_backend)
# We will import Resources , Api where we define them
# Here in this init file we will just register the blueprints
def create_api():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Importing models so that migrations can be applied
    from system.Models.User import User
    from system.Models.Video import Video
    from system.Models.Playlist import Playlist
    from system.Models.Likes import Likes
    from system.Models.Comments import Comments
    
    with app.app_context():
        db.init_app(app=app)
        mail.init_app(app)
        celery.conf.update(app.config)
        migrate.init_app(app,db)
    # register the blueprint
    from system.admin import admin
    app.register_blueprint(admin)

    from system.users import user
    app.register_blueprint(user , url_prefix="/users")
    # ctx = app.app_context()
    # ctx.push()
    return app