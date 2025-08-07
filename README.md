# vibe-coding

# vibe-coding

A simple Flask-based web API to fetch and display public GitHub gists for any user.  
This project includes CI/CD automation with Jenkins, Docker containerization, and Microsoft Teams notifications.

---

## Features

- **Flask API**: Exposes endpoints to fetch GitHub gists for a given username.
- **Dockerized**: Easily build and run the app in a container.
- **Automated Testing**: Uses `pytest` for unit tests.
- **CI/CD**: Jenkins pipeline for build, test, Docker image creation, and Teams notifications.

---

## Project Structure

```
vibe-coding/
├── app.py                # Flask app entry point
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container build instructions
├── Jenkinsfile           # CI/CD pipeline definition
├── webserver/
│   └── server.py         # Flask Blueprint for gist API
├── test/
│   └── test_app.py       # Example unit tests
└── README.md             # Project documentation
```

---

## Usage

### 1. Local Development

**Install dependencies:**
```sh
pip install --no-cache-dir -r requirements.txt
```

**Run the app:**
```sh
python app.py
```
The API will be available at [http://localhost:8080](http://localhost:8080).

**Example API call:**
```
GET /<username>
```
Returns a list of public gists for the specified GitHub user.

---

### 2. Running Tests

```sh
pytest --maxfail=1 --disable-warnings -q
```

---

### 3. Docker

**Build the Docker image:**
```sh
docker build -t flask-gist-app .
```

**Run the container:**
```sh
docker run -p 8080:8080 flask-gist-app
```

---

### 4. CI/CD with Jenkins

- The `Jenkinsfile` defines stages for checkout, install & test, Docker build, and Teams notifications.
- **Teams notifications**: Add your Teams webhook URL as a Jenkins secret text credential with the ID `teams-webhook-url`.

**Pipeline stages:**
- Checkout code from GitHub
- Install dependencies and run tests
- Build Docker image
- Notify Microsoft Teams on success or failure

---

## Example Code

**app.py**
```python
from flask import Flask
from webserver.server import gist_api

app = Flask(__name__)
app.register_blueprint(gist_api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

**webserver/server.py**
```python
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
```

---

## Requirements

- Python 3.11+
- Flask
- requests
- pytest (for testing)
- Docker (for containerization)
- Jenkins (for CI/CD)

---

## Teams Webhook Setup for Jenkins

1. In Microsoft Teams, create an **Incoming Webhook** connector and copy the URL.
2. In Jenkins, go to **Manage Jenkins → Manage Credentials**.
3. Add a new **Secret text** credential:
   - **Secret:** (paste your Teams webhook URL)
   - **ID:** `teams-webhook-url`
4. The Jenkins pipeline will use this credential for notifications.

---

## License

MIT License

---