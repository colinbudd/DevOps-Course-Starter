from config import KEY, TOKEN, USERNAME
import requests

board_id = 0
todo_list_id = 0
done_list_id = 0

BOARD_NAME = 'TODOv1'

"""
Initialisation
Check whether board exists. If board exists then obtain the board and list IDs.

If board does not exist then create board and loop
"""
while board_id == 0:
    boards = requests.get('https://api.trello.com/1/members/{USERNAME}/boards?key={KEY}}&token={TOKEN}').json()
    for board in boards:
        if board['name'] == BOARD_NAME:
            board_id == board['id']
            lists = requests.get('https://api.trello.com/1/boards/{board_id}/lists?key={KEY}}&token={TOKEN}').json()
            for list in lists:
                if list['name'] == 'To Do':
                    todo_list_id = list['id']
                elif list['name'] == 'Done':
                    done_list_id = list['id']
    if board_id == 0:
        requests.post('https://api.trello.com/1/boards/?key={KEY}}&token={TOKEN}&name={BOARD_NAME}')


def get_items():
    """
    Fetches all saved items from Trello.

    Returns:
        list: The list of saved items.
    """
    return session.get('items', _DEFAULT_ITEMS)


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):
    """
    Adds a new item with the specified title to the board.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    items.append(item)
    session['items'] = items

    return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item


def remove_item(id):
    """
    Deletes an existing item from the session. If no existing item matches the ID of the specified item, nothing is deleted.

    Args:
        id: The ID of the item.
    """
    items = get_items()
    for index, item in enumerate(session['items']):
        if item['id'] == int(id):
            del items[index]
            break

    del session['items']
    session['items'] = items
