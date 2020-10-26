from todo_item import Status

class ViewModel:
    def __init__(self, items):
        self._items = items
        self._show_all_done_items = False

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

    @property
    def recent_done_items(self):
        return ViewModel.filter_items_after_date(self.done_items, now)

    @property
    def older_done_items(self):
        return ViewModel.filter_items_before_date(self.done_items, now)

    @staticmethod
    def filter_items_before_date(items, date):
        return [n for n in items if n.due_raw < date]

    @staticmethod
    def filter_items_after_date(items, date):
        return [n for n in items if n.due_raw >= date]

