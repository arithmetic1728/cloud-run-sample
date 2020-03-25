import os

from flask import Flask
import requests
import google.auth.transport.requests
from google.oauth2 import id_token

app = Flask(__name__)

REQUESTS_SESSION = requests.Session()
REQUESTS_SESSION.verify = False
http_request = google.auth.transport.requests.Request(REQUESTS_SESSION)


@app.route("/")
def hello_world():
    try:
        token = id_token.fetch_id_token(http_request, "https://pubsub.googleapis.com")
    except Exception as e:
        return str(e)
    # return credentials.token
    return token


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
