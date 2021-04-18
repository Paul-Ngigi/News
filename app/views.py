from flask import render_template
from app import app


@app.route('/')
def index():
    title = 'Home - Welcome to News Article'
    return render_template('index.html', title=title)
