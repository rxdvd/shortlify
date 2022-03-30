from flask import Flask, render_template, request
from werkzeug import exceptions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
