import os

from cs50 import SQL

from flask import Flask
from flask_session import Session

app = Flask(__name__)

# Create an instance of the SQL class with the engine
db_uri = "sqlite:///schoolboard.db"
db = SQL(db_uri)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

def create_app(KEY):
    app.config["SECRET_KEY"] = KEY
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    
    Session(app)

    from .views import views
    from .auth import auth

    create_database()

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app


def create_database():
    if os.path.exists('schoolboard.db'):
        users = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER,
                username TEXT unique,
                email TEXT unique,
                city TEXT,
                password TEXT,
                date DATE ,
                category TEXT,
                PRIMARY KEY(id)
            )
        """

        db.execute(users)


if __name__ == "__main__":
    create_app(os.getenv("KEY"))