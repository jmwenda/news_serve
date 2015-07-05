from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form


from flask_wtf import Form
from wtforms import TextAreaField, TextField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from .models import Story

class StoryForm(Form):
    text = TextAreaField('text',
                    validators=[DataRequired(), Length(min=3, max=10000)])
    title = TextField('title', validators=[DataRequired(), Length(min=3, max=10000)])
    slug = TextField('slug', validators=[DataRequired(), Length(min=3, max=10000)])
    def __init__(self, *args, **kwargs):
        super(StoryForm, self).__init__(*args, **kwargs)


    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        return True
