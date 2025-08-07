from flask import Blueprint, jsonify
import requests

gist_api = Blueprint("gist_api", __name__)

@gist_api.route("/<username>", methods=["GET"])
def get_gists(username):
    url = f"https://api.github.com/users/{username}/gists"
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": "User not found or GitHub API error"}), 404

    gists = [
        {
            "id": gist["id"],
            "description": gist["description"],
            "url": gist["html_url"]
        }
        for gist in response.json()
    ]
    return jsonify(gists)