from flask import Flask, sessions
from flask_session import Session

app = Flask(__name__)

def create_app(KEY):
    app.config["SECRET_KEY"] = KEY
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
