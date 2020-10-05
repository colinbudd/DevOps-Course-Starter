from flask import Flask, render_template, request, redirect, url_for, send_from_directory, json, redirect
from board import board

app = Flask(__name__)

app.config.from_object('flask_config.Config')

my_board = board()

def task_sorting_key(task):
    if (task.status == 'Completed'):
        return 1
    else:
        return 0

@app.route('/')
def index():
    return render_template('index.html', tasks = sorted(my_board.get_items(), key=task_sorting_key))

@app.route('/', methods=['POST'])
def add_todo():
    my_board.add_item(request.form.get('title'))
    return redirect('/', code=303)

# @app.route('/tasks/<id>', methods=['PATCH'])
# def update_todo(id):
#     if (request.form.get('action') == 'mark_complete'):
#         item = board.get_item(id)
#         item['status'] = 'Completed'
#         board.save_item(item)
#     return json.dumps({'success':True}), 200, {'Content-Type':'application/json'} 

@app.route('/tasks/<id>', methods=['DELETE'])
def remove_todo(id):
    my_board.remove_item(id)
    return json.dumps({'success':True}), 200, {'Content-Type':'application/json'}

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == '__main__':
    app.run()
