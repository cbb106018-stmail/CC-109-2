import requests
from flask_wtf import Form, FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField, ValidationError, BooleanField

class FormRegister(Form):
    username = StringField('Username', validators=[
        validators.DataRequired(),
        validators.Length(5, 30)
    ])
    password = PasswordField('Password', validators=[
        validators.DataRequired(),
        validators.Length(5, 15),
        validators.EqualTo('password2', message='PASSWORD NEED MATCH')
    ])
    password2 = PasswordField('Confirm Password', validators=[
        validators.DataRequired()
    ])
    submit = SubmitField('Sign up')

    def validate_username(self, field):
        print(field.data)
        if self._check_username_existing(field.data):
            raise ValidationError('Username is duplicated.')

    def _check_username_existing(self, username):
        api_url = 'http://104.46.235.6/check_username_existing'
        param = {'username': username}
        res = requests.post(url=api_url, params=param)
        if res.json()!=None and res.json().get('success')==True:
            dup = res.json().get('duplicated')
        else:
            dep = False
        return dup
