import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_octocat_gists(client):
    response = client.get('/octocat')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert all('id' in gist and 'url' in gist for gist in data)