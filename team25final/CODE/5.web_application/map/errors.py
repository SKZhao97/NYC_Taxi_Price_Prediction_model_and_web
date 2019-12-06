from flask import render_template
from map import app

@app.errorhandler(404)	# Error page
def page_not_found(e):
    return render_template('errors/404.html'), 404