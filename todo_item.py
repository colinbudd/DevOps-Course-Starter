from config import KEY, TOKEN
import requests

class todo_item:

    def __init__(self, json):
        """
        Initialisation
        Construct a todo item from JSON
        """
        self._title = json['name']
        self._id = json['id']
        self._description = json['desc']
        list_json = requests.get(f'https://api.trello.com/1/cards/{self._id}/list?key={KEY}&token={TOKEN}').json()
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
    def status(self):
        return self._list
