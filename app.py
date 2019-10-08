from flask import Flask
from routes import init_api_routes
from routes import init_website_routes
from uuid import uuid4

app = Flask(__name__)
app.secret_key = str(uuid4())

init_api_routes(app)
init_website_routes(app)

if __name__ == "__main__":
    app.run(debug=True, port=1996)
