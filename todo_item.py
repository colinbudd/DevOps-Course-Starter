from config import KEY, TOKEN
import requests
from datetime import datetime

trello_auth_params = {"key": KEY, "token": TOKEN}

class TodoItem:

    def __init__(self, json):
        """
        Initialisation
        Construct a todo item from JSON
        """
        self._title = json['name']
        self._id = json['id']
        self._description = json['desc']
        self._due = json['due']
        if json['due']:
            self._due = datetime.strptime(json['due'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime("%A, %d %b %Y")
        list_json = requests.get(f'https://api.trello.com/1/cards/{self._id}/list', params=trello_auth_params).json()
        self._list = list_json['name']


    @property
    def title(self):
        return self._title

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @property
    def due(self):
        return self._due

    @property
    def status(self):
        return self._list
