from app.app import app
import pytest

@pytest.fixture
def setup_app():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config["SECRET_KEY"] = "test"
    return app

def test_app_running(setup_app):
    with setup_app.test_client() as client:
        response = client.get("/page2")
        assert response.status_code == 200

def test_app_visible(setup_app):
    with setup_app.test_client() as client:
        response = client.get("/page2")
        assert b'Welcome to the page 2' in response.data