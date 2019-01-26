from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Ada'}
	return render_template("index.html", title = "Welcome to Health Hacc!", user = user)
