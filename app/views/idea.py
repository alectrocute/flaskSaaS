from flask import (Blueprint, render_template, redirect, request, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required, current_user
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
from app.forms import Idea as idea_forms
from app.toolbox import email
# Setup Stripe integration
import stripe
import json
from json import dumps

# Create a user blueprint
ideabp = Blueprint('ideabp', __name__, url_prefix='/idea')

@ideabp.route('/new', methods=['GET', 'POST'])
def new():
    form = idea_forms.New()
    if form.validate_on_submit():
        print("test")
        # Create a user who hasn't validated his email address
        idea = models.Idea(
            title=form.title.data
        )
        # Insert the user in the database
        db.session.add(idea)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('idea/new.html', form=form, title='New Idea')