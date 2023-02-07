from datetime import datetime
from flask import Flask, render_template, request
import json

db_name = 'db.json'


def load_info(db_name):
    with open(db_name, 'r') as db:
        db_info = json.load(db)
    return db_info['messages']


def save_info(db_info, db_name):
    data = {'messages': db_info}
    with open(db_name, 'w') as json_file:
        json.dump(data, json_file)


app = Flask(__name__)

all_messages = load_info(db_name)
@app.route('/index')
def index_page():
    return "Hello world!"

@app.route("/chat")
def display_chat():
    return render_template('form.html')

@app.route('/get_messages')
def get_message():
    return {'messages': all_messages}

@app.route('/send_message')
def send_message():
    sender = request.args['name']
    text = request.args['text']
    time = datetime.now().strftime('%H:%M')
    text_info = {
        'text': text,
        'sender': sender,
        'time': time
    }
    all_messages.append(text_info)
    save_info(all_messages, db_name)



app.run(host='0.0.0.0', port=5050)