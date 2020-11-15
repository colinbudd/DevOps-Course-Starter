from todo_item import Status
from datetime import date

class ViewModel:
    def __init__(self, items, show_all_done_items):
        self._items = items
        self._show_all_done_items = show_all_done_items == "True"

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        return [n for n in self._items if n.status == Status.TODO]

    @property
    def doing_items(self):
        return [n for n in self._items if n.status == Status.DOING]

    @property
    def done_items(self):
        return [n for n in self._items if n.status == Status.DONE]

    @property
    def show_all_done_items(self):
        return self._show_all_done_items

    @show_all_done_items.setter
    def show_all_done_items(self, new_value):
        self._show_all_done_items = new_value

    def recent_done_items(self, comparison_date = date.today()):
        return [n for n in self.done_items if n.last_activity >= comparison_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')]

    def older_done_items(self, comparison_date = date.today()):
        return [n for n in self.done_items if n.last_activity < comparison_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')]
