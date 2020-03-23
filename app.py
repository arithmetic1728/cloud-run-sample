import os

from flask import Flask
import requests
import google.auth.transport.requests
import google.auth.compute_engine

app = Flask(__name__)

REQUESTS_SESSION = requests.Session()
REQUESTS_SESSION.verify = False
http_request = google.auth.transport.requests.Request(REQUESTS_SESSION)


@app.route("/")
def hello_world():
    credentials = google.auth.compute_engine.IDTokenCredentials(
        http_request, "target_audience", use_metadata_identity_endpoint=True
    )
    try:
        credentials.refresh(http_request)
    except Exception as e:
        return str(e)
    #return credentials.token
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
