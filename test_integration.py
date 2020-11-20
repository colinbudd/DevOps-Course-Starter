import pytest
import requests
from dotenv import find_dotenv, load_dotenv
from app import create_app


class MockResponse(object):
    def __init__(self, json):
        self.response_json = json

    def json(self):
        return self.response_json


@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = create_app('test-todo-list-id', 'test-doing-list-id', 'test-done-list-id')

    # Use the app to create a test_client that can be used in our tests.
    test_app.testing = True
    with test_app.test_client() as client:
        yield client


def test_index_page(monkeypatch, client):

    # Arrange
    def mock_get(url, params):
        assert url == f'https://api.trello.com/1/boards/trello-board-id/cards'
        assert params['key'] == 'trello-key'
        assert params['token'] == 'trello-token'
        return MockResponse(
            [
                {
                    "name": "test-item-1",
                    "id": "test-id-1",
                    "desc": "test-description-1",
                    "due": "2020-12-25T12:00:00.000000Z",
                    "dateLastActivity": "2020-10-25T12:00:00.000000Z",
                    "idList": "test-todo-list-id"
                },
                {
                    "name": "test-item-2",
                    "id": "test-id-2",
                    "desc": "test-description-2",
                    "due": "2020-12-26T12:00:00.000000Z",
                    "dateLastActivity": "2020-10-26T12:00:00.000000Z",
                    "idList": "test-doing-list-id"
                }
            ])


    monkeypatch.setattr(requests, "get", mock_get)

    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == 200

    decoded_response = response.data.decode('utf-8')

    assert "test-item-1" in decoded_response
    assert "test-item-2" in decoded_response
