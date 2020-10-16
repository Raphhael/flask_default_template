from wtforms import StringField
from wtforms.validators import Required, Optional
from flask_security.forms import RegisterForm, LoginForm


class ExtendedRegisterForm(RegisterForm):
    username = StringField('Pseudo', [Required()])
    email = StringField('Adresse e-mail', [Optional()])


class ExtendedLoginForm(LoginForm):
    email = StringField('Pseudo', [Required()])
