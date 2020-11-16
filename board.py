import requests
import os
from todo_item import TodoItem, Status

class Board:

    def __init__(self):
        """
        Initialisation
        Check whether board exists. If board exists then obtain the board and list IDs.

        If board does not exist then create board and repeat loop to obtain IDs.
        """
        self.trello_auth_params = {"key": os.environ['TRELLO_KEY'], "token": os.environ['TRELLO_TOKEN']}
        self.board_id = 0
        while self.board_id == 0:
            boards = requests.get(f'https://api.trello.com/1/members/{os.environ["TRELLO_USERNAME"]}/boards', params=self.trello_auth_params).json()
            for board in boards:
                if board['name'] == os.environ['TRELLO_BOARD_NAME']:
                    self.board_id = board['id']
                    lists = requests.get(f'https://api.trello.com/1/boards/{self.board_id}/lists', params=self.trello_auth_params).json()
                    for list in lists:
                        if list['name'].lower() == 'to do':
                            self.todo_list_id = list['id']
                        elif list['name'].lower() == 'done':
                            self.done_list_id = list['id']
                        elif list['name'].lower() == 'doing':
                            self.doing_list_id = list['id']
            if self.board_id == 0:
                print(f'Creating new board')
                post_params = self.trello_auth_params.copy()
                post_params['name'] = os.environ['TRELLO_BOARD_NAME']
                requests.post(f'https://api.trello.com/1/boards/', params=post_params)


    def list_to_status(self, list_id):
        if list_id == self.todo_list_id:
            return Status.TODO
        elif list_id == self.doing_list_id:
            return Status.DOING
        elif list_id == self.done_list_id:
            return Status.DONE


    def get_items(self):
        """
        Fetches all TODO items.

        Returns:
            list: The list of saved items.
        """
        items_json = requests.get(f'https://api.trello.com/1/boards/{self.board_id}/cards', params=self.trello_auth_params).json()
        items = []
        for item in items_json:
            items.append(TodoItem(item, self.list_to_status(item['idList'])))
        return items


    def add_item(self, title, description, due):
        """
        Adds a new item with the specified title and description to the board.

        Args:
            title: The title of the item.
        """
        post_params = self.trello_auth_params.copy()
        post_params['idList'] = self.todo_list_id
        post_params['name'] = title
        post_params['desc'] = description

        if due:
            post_params['due'] = due

        requests.post(f'https://api.trello.com/1/cards', params=post_params)


    def move_item(self, id, targetList):
        """
        Removes an item from one list and then adds a copy to a target list.

        Args:
            id: The ID of the item.
            targetList: The target list to add the item to.
        """
        item_json = requests.get(f'https://api.trello.com/1/cards/{id}', params=self.trello_auth_params).json()
        requests.delete(f'https://api.trello.com/1/cards/{id}', params=self.trello_auth_params)

        post_params = self.trello_auth_params.copy()
        post_params['name'] = item_json['name']
        post_params['desc'] = item_json['desc']

        if (targetList == "DOING"):
            post_params['idList'] = self.doing_list_id
        else:
            post_params['idList'] = self.done_list_id

        if item_json['due']:
            post_params['due'] = item_json['due']

        requests.post(f'https://api.trello.com/1/cards', params=post_params)


    def remove_item(self, id):
        """
        Deletes an existing item from the board.

        Args:
            id: The ID of the item.
        """
        requests.delete(f'https://api.trello.com/1/cards/{id}', params=self.trello_auth_params)
