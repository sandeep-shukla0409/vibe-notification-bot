from flask import Flask
from webserver.server import gist_api
import json

# Set up a minimal Flask app for testing
app = Flask(__name__)
app.register_blueprint(gist_api)
client = app.test_client()

def test_get_gists_for_octocat():
    response = client.get("/octocat")
    assert response.status_code == 200, "Expected 200 OK response"

    data = json.loads(response.data)
    assert isinstance(data, list), "Expected response to be a list"

    for gist in data:
        assert "id" in gist, "Each gist should have an 'id'"
        assert "description" in gist, "Each gist should have a 'description'"
        assert "url" in gist, "Each gist should have a 'url'"