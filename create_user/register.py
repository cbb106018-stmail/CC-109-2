from flask import Flask, request, json, jsonify, make_response
from flasgger import Swagger, swag_from
from sender import pass_on

app = Flask(__name__)

swagger = Swagger(app)

@app.route('/create_user', methods=['POST'])
@swag_from('apidocs/api_create_user.yml')
def create_user():
    isExistingData = False
    isRequestCompleted = False
    user_info = dict()

    jsonobj = request.get_json()
    if jsonobj != None:
        isExistingData = True
        username = json.dumps(jsonobj['username']).replace("\"", "")
        password = json.dumps(jsonobj['password']).replace("\"", "")
    elif request.values.get('username')!=None and request.values.get('password')!=None:
        isExistingData = True
        username = request.values.get('username')
        password = request.values.get('password')

    res = dict()
    if isExistingData:
        user_info['username'] = username
        user_info['password'] = password
        isRequestCompleted = pass_on(user_info) or False

        if isRequestCompleted:
            res['success'] = True
            res['message'] = 'User created successfully: ' + username + ' .'
            res = make_response(jsonify(res), 200)
        else:
            res['success'] = False
            res['message'] = 'Error occurred when proccessing request.'
    else:
        res['success'] = False
        res['message'] = 'Error occurred when parsing data.'
        res = make_response(jsonify(res), 500)
    return res

@app.route('/', methods=['POST'])
def index():
    jsonobj = request.get_json(silent=True)
    msg = json.dumps(jsonobj['message']).replace("\"", "") or "empty"
    res = dict()
    res['success'] = True
    res['message'] = 'Hello from index, and this is the message you just left: ' + msg
    res = make_response(jsonify(res), 200)
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
