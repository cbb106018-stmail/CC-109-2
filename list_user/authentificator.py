from flask import Flask, request, json, jsonify, make_response
from flasgger import Swagger, swag_from

app = Flask(__name__)

swagger = Swagger(app)

@app.route('/list_user', methods=['GET'])
@swag_from('apidocs/api_list_user.yml')
def list_user():
    res = dict()
    res['username_1'] = 'Daniel'
    res['username_2'] = 'Taylor'
    res['username_3'] = 'Jacob'
    res = make_response(jsonify(res), 200)
    return res

@app.route('/', methods=['GET'])
def index():
    res = dict()
    res['message'] = 'GET'
    res = make_response(jsonify(res), 200)
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
