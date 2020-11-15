"""Trello configuration class."""
import os

class TrelloConfig:
    """Base configuration variables."""
    TOKEN = os.environ['TRELLO_TOKEN']
    KEY = os.environ['TRELLO_KEY']
    USERNAME = os.environ['TRELLO_USERNAME']
    BOARD_NAME = os.environ['TRELLO_BOARD_NAME']
