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

    @property
    def title(self):
        return self._title

    @property
    def id(self):
        return self._id

    @property
    def status(self):
        return "Completed"
