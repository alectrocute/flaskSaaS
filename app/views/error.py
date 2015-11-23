from flask import render_template
from app import app


@app.errorhandler(403)
def forbidden(e):
    return render_template('error.html', message='403 forbidden'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message='404 not found'), 404


@app.errorhandler(410)
def gone(e):
    return render_template('error.html', message='410 gone'), 410


@app.errorhandler(500)
def internal_error(e):
    return render_template('error.html', message='500 internal error'), 500
