from flask import Flask, request, json, jsonify, make_response
from flasgger import Swagger, swag_from
from passing_query import listing_user, checking_username

app = Flask(__name__)

swagger = Swagger(app)

@app.route('/list_users', methods=['GET'])
@swag_from('apidocs/api_list_user.yml')
def list_users():
    res = dict()
    res['username_1'] = 'Daniel'
    res['username_2'] = 'Taylor'
    res['username_3'] = 'Jacob'
    res = make_response(jsonify(res), 200)
    return res

@app.route('/check_username_isused', method=['GET', 'POST'])
@swag_from('apidocs/api_check_username_isused.yml')
def check_username_isused():
    isExistingData = False
    user_input_name = ''

    jsonobj = request.get_json()
    if jsonobj != None:
        isExistingData = True
        user_input_name = json.dumps(jsonobj['username']).replace("\"", "")
    elif request.values.get('username')!=None:
        isExstingData = True
        user_input_name = request.values.get('username')

    res = dict()
    if isExistingData:
        isUsernameDuplicated = checking_username(username) or True
        res['success'] = True
        if not isUsernameDuplicated:
            res['duplicated'] = False
            res['message'] = 'Username "' + user_input_name + '" is not in use.'
        else:
            res['duplicated'] = True
            res['message'] = 'Username "' + user_input_name + '" is duplicated.'
        res = make_response(jsonify(res), 200)
    else:
        res['success'] = False
        res['duplicated'] = True
        res['message'] = 'Error occured when parsing request value.'
        res = make_response(jsonify(res), 500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
