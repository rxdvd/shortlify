from flask import Flask, render_template, request, jsonify, redirect
from werkzeug import exceptions
from db_config import get_collection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
