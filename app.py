from flask import Flask, render_template, request, redirect, url_for, send_from_directory, json, redirect
from board import Board
from view_model import ViewModel
from todo_item import Status
from datetime import date, datetime

def create_app(board_id=0, todo_list_id=0, doing_list_id=0, done_list_id=0):
    app = Flask(__name__)
    app.config.from_object('flask_config.Config')

    my_board = Board(board_id, todo_list_id, doing_list_id, done_list_id)

    def task_sorting_key(task):
        if (task.status == Status.DONE):
            return 1
        else:
            return 0

    #pylint: disable=unused-variable

    @app.route('/')
    def index():
        item_view_model = ViewModel(sorted(my_board.get_items(), key=task_sorting_key)) 
        item_view_model.show_all_done_items = request.cookies.get('showAllDoneItems') == 'True'
        return render_template('index.html', view_model = item_view_model, today = date.today())

    @app.route('/', methods=['POST'])
    def add_todo():
        if request.form.get('due'):
            due_obj = datetime.strptime(request.form.get('due'), '%d/%m/%Y')
        else:
            due_obj = None
        my_board.add_item(request.form.get('title'), request.form.get('description'), due_obj)
        return redirect('/', code=303)

    @app.route('/tasks/<id>', methods=['PATCH'])
    def update_todo(id):
        my_board.move_item(id, request.form.get('targetList'))
        return json.dumps({'success':True}), 200, {'Content-Type':'application/json'} 

    @app.route('/tasks/<id>', methods=['DELETE'])
    def remove_todo(id):
        my_board.remove_item(id)
        return json.dumps({'success':True}), 200, {'Content-Type':'application/json'}

    @app.route('/js/<path:path>')
    def send_js(path):
        return send_from_directory('js', path)

    #pylint: enable=unused-variable
    
    return app


app = create_app()

if __name__ == '__main__':
    app.run()
