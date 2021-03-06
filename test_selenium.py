import os
import pytest
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from app import create_app
from board import create_trello_board, delete_trello_board


@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable
    board_id = create_trello_board()
    os.environ['TRELLO_BOARD_ID'] = board_id 

    # construct the new application
    application = create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application

    # Tear Down
    thread.join(1)
    delete_trello_board(board_id)


@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')

    driver.implicitly_wait(10)

    assert driver.title == 'To-Do App'

    todo_title = 'Test Todo Item'
    todo_description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    # Create new item

    driver.find_element_by_id('title').send_keys(todo_title)
    driver.find_element_by_id('description').send_keys(todo_description)
    driver.find_element_by_id('add-new-todo').click()

    # Check the new item

    card = get_card_with_title(driver, 'todo-list', todo_title)
    
    description = card.find_element_by_class_name('todo-description').text
    assert description == todo_description

    # Click the start button

    card.find_element_by_class_name('move-doing-list').click()

    # Check the started item

    card = get_card_with_title(driver, 'doing-list', todo_title)
    
    description = card.find_element_by_class_name('todo-description').text
    assert description == todo_description

    # Click the complete button

    card.find_element_by_class_name('move-done-list').click()

    # Check the completed item

    card = get_card_with_title(driver, 'done-list', todo_title)
    
    description = card.find_element_by_class_name('todo-description').text
    assert description == todo_description



# Helper methods

def condition_to_find_element_with_title(list_id, title):
    return expected_conditions.presence_of_element_located((By.XPATH, f'//*[@id="{list_id}"]//*[contains(@class, "todo-title")][text() = "{title}"]'))

def get_card_with_title(driver, list_id, title):
    return driver.find_element_by_xpath(f'//*[@id="{list_id}"]//*[contains(@class, "todo-title")][text() = "{title}"]/ancestor::*[contains(@class, "todo-item")]')
