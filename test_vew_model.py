from view_model import ViewModel
from todo_item import TodoItem, Status
from datetime import date
import pytest


todo_item_1_name = "todo item 1"
todo_item_1_id = "d7c1d402-899c-4bce-9988-5036417d47de"
todo_item_1_desc = "description for first todo item"
todo_item_1_due = "2020-10-24T01:01:01.000000Z"
todo_item_1_last_activity = "2020-10-20T01:01:01.000000Z"
todo_item_2_name = "todo item 2"
todo_item_2_id = "a4f3f21d-e04d-42e6-a6ed-63290b80d654"
todo_item_2_desc = "description for second todo item"
todo_item_2_due = "2020-10-24T02:02:02.000000Z"
todo_item_2_last_activity = "2020-10-20T02:02:02.000000Z"
doing_item_1_name = "doing item 1"
doing_item_1_id = "2f464251-68a7-4307-973e-c17cb1acc0a3"
doing_item_1_desc = "description for first doing item"
doing_item_1_due = "2020-10-24T03:03:03.000000Z"
doing_item_1_last_activity = "2020-10-20T03:03:03.000000Z"
doing_item_2_name = "doing item 2"
doing_item_2_id = "fa506c9a-a8a0-4ef5-9790-789350c9d551"
doing_item_2_desc = "description for second doing item"
doing_item_2_due = "2020-10-24T04:04:04.000000Z"
doing_item_2_last_activity = "2020-10-20T04:04:04.000000Z"
done_item_1_name = "done item 1"
done_item_1_id = "f5ffb57d-d2cc-481d-bfaa-46c5349de175"
done_item_1_desc = "description for first done item"
done_item_1_due = "2020-10-24T05:05:05.000000Z"
done_item_1_last_activity = "2020-10-20T01:01:01.000000Z"
done_item_2_name = "done item 2"
done_item_2_id = "16c4cae4-e7ef-4a32-8677-fefc0a8406fa"
done_item_2_desc = "description for second done item"
done_item_2_due = "2020-10-24T06:06:06.000000Z"
done_item_2_last_activity = "2020-10-19T23:59:59.000000Z"

todo_item_1 = TodoItem({"name": todo_item_1_name, "id": todo_item_1_id, "desc": todo_item_1_desc, "due": todo_item_1_due, "dateLastActivity": todo_item_1_last_activity}, Status.TODO)
todo_item_2 = TodoItem({"name": todo_item_2_name, "id": todo_item_2_id, "desc": todo_item_2_desc, "due": todo_item_2_due, "dateLastActivity": todo_item_2_last_activity}, Status.TODO)
doing_item_1 = TodoItem({"name": doing_item_1_name, "id": doing_item_1_id, "desc": doing_item_1_desc, "due": doing_item_1_due, "dateLastActivity": doing_item_1_last_activity}, Status.DOING)
doing_item_2 = TodoItem({"name": doing_item_2_name, "id": doing_item_2_id, "desc": doing_item_2_desc, "due": doing_item_2_due, "dateLastActivity": doing_item_2_last_activity}, Status.DOING)
done_item_1 = TodoItem({"name": done_item_1_name, "id": done_item_1_id, "desc": done_item_1_desc, "due": done_item_1_due, "dateLastActivity": done_item_1_last_activity}, Status.DONE)
done_item_2 = TodoItem({"name": done_item_2_name, "id": done_item_2_id, "desc": done_item_2_desc, "due": done_item_2_due, "dateLastActivity": done_item_2_last_activity}, Status.DONE)


@pytest.fixture
def view_model():
    items = [todo_item_1, todo_item_2, doing_item_1, doing_item_2, done_item_1, done_item_2]
    view_model = ViewModel(items)
    return view_model


def test_get_todo_items(view_model):
    
    # Act
    todo_items = view_model.todo_items

    # Assert
    assert len(todo_items) == 2
    assert todo_item_1 in todo_items
    assert todo_item_2 in todo_items


def test_get_doing_items(view_model):

    # Act
    doing_items = view_model.doing_items

    # Assert
    assert len(doing_items) == 2
    assert doing_item_1 in doing_items
    assert doing_item_2 in doing_items


def test_get_done_items(view_model):
    
    # Act
    done_items = view_model.done_items

    # Assert
    assert len(done_items) == 2
    assert done_item_1 in done_items
    assert done_item_2 in done_items


def test_show_all_done_items():

    view_model = ViewModel([])

    assert view_model.show_all_done_items == False

    view_model.show_all_done_items = True

    assert view_model.show_all_done_items == True

    view_model.show_all_done_items = False

    assert view_model.show_all_done_items == False

def test_recent_done_items(view_model):

    # Act
    recent_done_items = view_model.recent_done_items(comparison_date = date(2020, 10, 20))

    # Assert
    assert len(recent_done_items) == 1
    assert done_item_1 in recent_done_items


def test_older_done_items(view_model):

    # Act
    older_done_items = view_model.older_done_items(comparison_date = date(2020, 10, 20))

    # Assert
    assert len(older_done_items) == 1
    assert done_item_2 in older_done_items

