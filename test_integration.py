import pytest
from dotenv import find_dotenv, load_dotenv
import requests
from app import create_app

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = create_app()

    # Use the app to create a test_client that can be used in our tests.
    test_app.testing = True
    with test_app.test_client() as client:
        yield client

def test_index_page(monkeypatch, client):

    def mock_get(url, params):
        #assert url == f'https://api.trello.com/1/boards/{self.board_id}/cards'
        assert params.key == 'trello-key'
        assert params.token == 'trello-token'
        return ["TODO"]

    monkeypatch.setattr(requests, "get", mock_get)

    # Act
    response = client.get('/')

    # Assert
    assert response.data != "TODO"
