from view_model import ViewModel
from todo_item import TodoItem, Status
import pytest

todo_item_1_name = "todo item 1"
todo_item_1_id = "d7c1d402-899c-4bce-9988-5036417d47de"
todo_item_1_desc = "description for first todo item"
todo_item_1_due = "2020-10-24T01:01:01.000Z"
todo_item_2_name = "todo item 2"
todo_item_2_id = "a4f3f21d-e04d-42e6-a6ed-63290b80d654"
todo_item_2_desc = "description for second todo item"
todo_item_2_due = "2020-10-24T02:02:02.000Z"
doing_item_1_name = "doing item 1"
doing_item_1_id = "2f464251-68a7-4307-973e-c17cb1acc0a3"
doing_item_1_desc = "description for first doing item"
doing_item_1_due = "2020-10-24T03:03:03.000Z"
doing_item_2_name = "doing item 2"
doing_item_2_id = "fa506c9a-a8a0-4ef5-9790-789350c9d551"
doing_item_2_desc = "description for second doing item"
doing_item_2_due = "2020-10-24T04:04:04.000Z"
done_item_1_name = "done item 1"
done_item_1_id = "f5ffb57d-d2cc-481d-bfaa-46c5349de175"
done_item_1_desc = "description for first done item"
done_item_1_due = "2020-10-24T01:01:01.000Z"
done_item_2_name = "done item 2"
done_item_2_id = "16c4cae4-e7ef-4a32-8677-fefc0a8406fa"
done_item_2_desc = "description for second done item"
done_item_2_due = "2020-10-24T02:02:02.000Z"

@pytest.fixture
def view_model_with_tasks():
    todo_item_1 = TodoItem({"name": todo_item_1_name, "id": todo_item_1_id, "desc": todo_item_1_desc, "due": todo_item_1_due}, Status.TODO)
    todo_item_2 = TodoItem({"name": todo_item_2_name, "id": todo_item_2_id, "desc": todo_item_2_desc, "due": todo_item_2_due}, Status.TODO)
    doing_item_1 = TodoItem({"name": doing_item_1_name, "id": doing_item_1_id, "desc": doing_item_1_desc, "due": doing_item_1_due}, Status.DOING)
    doing_item_2 = TodoItem({"name": doing_item_2_name, "id": doing_item_2_id, "desc": doing_item_2_desc, "due": doing_item_2_due}, Status.DOING)
    done_item_1 = TodoItem({"name": done_item_1_name, "id": done_item_1_id, "desc": done_item_1_desc, "due": done_item_1_due}, Status.DONE)
    done_item_2 = TodoItem({"name": done_item_2_name, "id": done_item_2_id, "desc": done_item_2_desc, "due": done_item_2_due}, Status.DONE)

    return ViewModel([todo_item_1, todo_item_2, doing_item_1, doing_item_2, done_item_1, done_item_2])


def test_get_todo_items(view_model_with_tasks):

    # Act
    todo_items = view_model_with_tasks.todo_items()

    # Assert
    assert len(todo_items) == 2
    assert "hello" in todo_items
