from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

app.run(host='0.0.0.0', port=80)