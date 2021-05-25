from flask import Flask, request, json, jsonify, make_response
from flasgger import Swagger, swag_from
from sender import pass_on

app = Flask(__name__)

swagger = Swagger(app)

@app.route('/create_user', methods=['POST'])
@swag_from('apidocs/api_create_user.yml')
def create_user():
    jsonobj = json.loads(request.data, strict=False)
    if jsonobj != None:
        username = json.dumps(jsonobj['username']).replace("\"", "")
        password = json.dumps(jsonobj['password']).replace("\"", "")

        user_info = dict()
        user_info['username'] = username
        user_info['password'] = password
        pass_on(user_info)

        res = dict()
        res['success'] = True
        res['message'] = 'User created successfully: ' + username
        res = make_response(jsonify(res), 200)
    else:
        res = dict()
        res['success'] = False
        res['message'] = 'Parsing data error, please check posting data. ' + income_data
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
