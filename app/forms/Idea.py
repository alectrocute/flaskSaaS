from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import (Required, Length, Email, ValidationError,
                                EqualTo)
from app.models import Idea

class New(Form):
        title = TextField(validators=[Required(), Length(min=2)],
                     description='Title')