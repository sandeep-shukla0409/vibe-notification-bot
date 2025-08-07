# GitHub Gist API Server

A lightweight Flask-based web server that exposes a REST API to fetch public GitHub gists for a given username.

---

## 🚀 Features

- 🔍 Fetch public gists for any GitHub user
- 📦 Simple JSON response with `id`, `description`, and `url`
- 🧪 Includes automated test using `octocat` as sample data

---

## 📁 Project Structure
. ├── webserver/ │   └── server.py         # Flask blueprint with /<username> route ├── test/ │   └── test_server.py    # Automated test for API ├── requirements.txt      # Python dependencies └── README.md             # Project documentation


---

## 🛠️ Setup & Run

### 1. Clone the repo

```bash
git clone https://github.com/your-username/xxxxxx.git


## Docker command to build test and run
docker build -t equal-experts-stalwart-sturdy-witty-problem-3b025001aaec .

docker run --rm equal-experts-stalwart-sturdy-witty-problem-3b025001aaec pytest test/

docker run -p 8080:8080 equal-experts-stalwart-sturdy-witty-problem-3b025001aaec

## Local command
pip install -r requirements.txt

python app.py

curl http://localhost:8080/octocat