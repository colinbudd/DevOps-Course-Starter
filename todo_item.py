from config import KEY, TOKEN
from enum import Enum
from datetime import datetime

trello_auth_params = {"key": KEY, "token": TOKEN}


class Status(Enum):
    TODO = 1
    DOING = 2
    DONE = 3


class TodoItem:

    def __init__(self, json, status):
        """
        Initialisation
        Construct a todo item from JSON
        """
        self._status = status
        self._title = json['name']
        self._id = json['id']
        self._description = json['desc']
        self._due = json['due']
        if json['due']:
            self._due = datetime.strptime(json['due'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime("%A, %d %b %Y")

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
        return self._status
