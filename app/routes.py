from flask import render_template
from app import app
from app.forms import RetrievalForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Ada'}
        form = RetrievalForm()
	return render_template("index.html", title = "Welcome to Health Hacc!", user = user, form = form)
