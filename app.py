from flask import Flask
from webserver.server import gist_api

app = Flask(__name__)
app.register_blueprint(gist_api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)