from config import KEY, TOKEN, USERNAME, BOARD_NAME
import requests
from todo_item import TodoItem

class Board:

    def __init__(self):
        """
        Initialisation
        Check whether board exists. If board exists then obtain the board and list IDs.

        If board does not exist then create board and repeat loop to obtain IDs.
        """
        self.board_id = 0
        while self.board_id == 0:
            boards = requests.get(
                f'https://api.trello.com/1/members/{USERNAME}/boards',
                params={
                    "key": KEY,
                    "token": TOKEN
                }).json()
            for board in boards:
                if board['name'] == BOARD_NAME:
                    self.board_id = board['id']
                    lists = requests.get(
                        f'https://api.trello.com/1/boards/{self.board_id}/lists',
                        params={
                            "key": KEY,
                             "token": TOKEN
                        }).json()
                    for list in lists:
                        if list['name'].lower() == 'to do':
                            self.todo_list_id = list['id']
                        elif list['name'].lower() == 'done':
                            self.done_list_id = list['id']
            if self.board_id == 0:
                print(f'Creating new board')
                requests.post(
                    f'https://api.trello.com/1/boards/',
                    params={
                        "key": KEY,
                        "token": TOKEN,
                        "name": BOARD_NAME
                    })
        print(f'Board: {self.board_id}; todo: {self.todo_list_id}; done: {self.done_list_id}')


    def get_items(self):
        """
        Fetches all TODO items.

        Returns:
            list: The list of saved items.
        """
        items_json = requests.get(
            f'https://api.trello.com/1/boards/{self.board_id}/cards',
            params={
                "key": KEY, 
                "token": TOKEN
            }).json()
        items = []
        for item in items_json:
            items.append(TodoItem(item))
        return items


    def add_item(self, title, description, due):
        """
        Adds a new item with the specified title and description to the board.

        Args:
            title: The title of the item.
        """
        if due:
            requests.post(
                f'https://api.trello.com/1/cards',
                params={
                    "key": KEY, 
                    "token": TOKEN,
                    "idList": self.todo_list_id,
                    "name": title,
                    "desc": description,
                    "due": due
                })
        else:
            requests.post(
                f'https://api.trello.com/1/cards',
                params={
                    "key": KEY, 
                    "token": TOKEN,
                    "idList": self.todo_list_id,
                    "name": title,
                    "desc": description
                })            


    def complete_item(self, id):
        """
        Removes an item from the 'todo' list and then adds a copy to the 'done' list.

        Args:
            id: The ID of the item.
        """
        item_json = requests.get(
            f'https://api.trello.com/1/cards/{id}',
            params={
                "key": KEY, 
                "token": TOKEN
            }).json()
        item_name = item_json['name']
        item_desc = item_json['desc']
        item_due = item_json['due']
        requests.delete(
            f'https://api.trello.com/1/cards/{id}',
            params={
                "key": KEY,
                "token": TOKEN
            })
        if item_due:
            requests.post(
                f'https://api.trello.com/1/cards',
                params={
                    "key": KEY, 
                    "token": TOKEN,
                    "idList": self.done_list_id,
                    "name": item_name,
                    "desc": item_desc,
                    "due": item_due
                })
        else:
            requests.post(
                f'https://api.trello.com/1/cards',
                params={
                    "key": KEY, 
                    "token": TOKEN,
                    "idList": self.done_list_id,
                    "name": item_name,
                    "desc": item_desc
                })

    def remove_item(self, id):
        """
        Deletes an existing item from the board.

        Args:
            id: The ID of the item.
        """
        requests.delete(
            f'https://api.trello.com/1/cards/{id}', 
            params={
                "key": KEY, 
                "token": TOKEN
            })
