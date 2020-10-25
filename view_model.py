from todo_item import Status

class ViewModel:
    def __init__(self, items):
        self._items = items

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
