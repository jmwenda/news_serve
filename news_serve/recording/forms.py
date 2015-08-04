#from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form

from flask_wtf import Form
from wtforms import TextAreaField, TextField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from .models import Recording


class RecordForm(Form):
    text = TextAreaField('text',
                    validators=[Length(min=3, max=10000)])
    ready_to_broadcast = BooleanField()
    def __init__(self, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)


    def validate(self):
        initial_validation = super(RecordForm, self).validate()
        if not initial_validation:
            return False
        return True
