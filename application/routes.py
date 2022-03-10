from flask import render_template, request
from application import app

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')