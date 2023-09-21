import os
from src import create_app
from dotenv import load_dotenv
from flask_session import Session

load_dotenv()
KEY = os.getenv('SECRET_KEY')

app = create_app(KEY)

Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

if __name__ == "__main__":
    app.run(port=3000, debug=True)