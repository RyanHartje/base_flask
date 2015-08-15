
from wtforms import Form, StringField, TextAreaField, SelectField, SelectMultipleField, BooleanField, validators
from flask_security.forms import ConfirmRegisterForm
from wtforms.validators import Required

#from wtforms.csrf.session import SessionCSRF
from datetime import timedelta

class ExtendedConfirmRegisterForm(ConfirmRegisterForm):
  domain = StringField('domain')
  name = StringField('name')

