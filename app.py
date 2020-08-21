from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    return render_template('index.html', tasks = session.get_items())

@app.route('/', methods=['POST'])
def add_todo():
    session.add_item(request.form.get('title'))
    return index()

if __name__ == '__main__':
    app.run()
