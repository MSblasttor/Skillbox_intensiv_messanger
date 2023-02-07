from datetime import datetime
from flask import Flask, render_template, request
import json

db_name = 'db_json'

def load_info(db_name):
    with open(db_name, 'r') as db:
        db_info = json.load(db)
    return db_info

app = Flask(__name__)

@app.route('/index')
def index_page():
    return "Hello world!"

@app.route("/chat")
def display_chat():
    return render_template('form.html')

app.run(host='0.0.0.0', port=80)