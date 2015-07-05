from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form


from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from ..story.models import Story

class TranslationForm(Form):
    text = TextAreaField('text',
                    validators=[DataRequired(), Length(min=3, max=10000)])
    def __init__(self, *args, **kwargs):
        super(TranslationForm, self).__init__(*args, **kwargs)


    def validate(self):
        initial_validation = super(TranslationForm, self).validate()
        if not initial_validation:
            return False
        return True
