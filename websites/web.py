import requests
from flask import Flask, render_template, request, json
from flask_bootstrap import Bootstrap
from form import FormRegister
from werkzeug.security import generate_password_hash, check_password_hash
import os
from config import Config

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = "b'\xe2\xc5\x83\xbd=\xc1\x14\x0b\x0e\xb1\r\x08\xe5\x04\xcd\xf8\xac\xf7\xbe\xa3\xf5\x83\xc9\xc0'"
app.config.from_pyfile('config.py')
SESSION_PROTECTION = 'strong'

@app.route('/web/register', methods=['GET', 'POST'])
def register():
    form = FormRegister()
    if form.validate_on_submit():
        user = {
                'username': form.username.data,
                'password': generate_password_hash(form.password.data)
                }

        api_url = 'http://104.46.235.6/create_user'
        resp = requests.post(url=api_url, params=user)
        if resp != None:
            res = {'message': resp.json().get('message'), 'success': resp.json().get('success')}
        else:
            res = {'message': 'Request error.', 'success': False}
        return res
    return render_template('register.html', form=form)

@app.route('/login')
def login():
    return 'Here is Login'

@app.route('/logout')
def logout():
    return 'Logout'

@app.route('/userinfo')
def userinfo():
    return 'Here is UserInfo'

@app.route('/web/index')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
