import os
from src import create_app

KEY = os.getenv("SECRET_KEY")
app = create_app(KEY)

if __name__ == "__main__":
    app.run(host="0.0.0.0{}", port=3000, debug=True, load_dotenv=True)