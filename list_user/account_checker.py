from flask import Flask, request, json, jsonify, make_response
from flasgger import Swagger, swag_from
from passing_query import listing_user, is_username_existing

app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'APIDOCS for list_users',
    'uiversion': 3
}

swagger_config = {
    "headers": [
        ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
    "url_prefix": "/api/list_users"
}

swagger = Swagger(app, config=swagger_config)

@app.route('/list_users', methods=['GET'])
@swag_from('apidocs/api_list_user.yml')
def list_users():
    res = dict()
    #res['username_1'] = 'Daniel'
    #res['username_2'] = 'Taylor'
    #res['username_3'] = 'Jacob'
    #res = make_response(jsonify(res), 200)
    userLists = listing_user()
    if userLists == None:
        res['message'] = 'No data existing.'
        res['success'] = False
        res['userlist'] = {}
        res = make_response(jsonify(res), 500)
    elif type(userLists) == list:
        res['message'] = 'Query executed successful.'
        res['success'] = True
        userlist = dict()
        for user in range(0, len(userLists)):
            userlist['user_'+str(user+1)] = userLists[user]
        #res['userlist'] = json.dumps(userlist).replace("\"", "\'")
        res['userlist'] = userlist
        res = make_response(jsonify(res), 200)
    return res

@app.route('/check_username_existing', methods=['GET', 'POST'])
@swag_from('apidocs/api_is_username_existing.yml')
def check_username_existing():
    isExistingData = False
    user_input_name = None

    jsonobj = request.get_json()
    if jsonobj != None:
        isExistingData = True
        user_input_name = json.dumps(jsonobj['username']).replace("\"", "")
    elif request.values.get('username') != None:
        isExistingData = True
        user_input_name = request.values.get('username')
    elif request.args.get('username') != None:
        isExistingData = True
        user_input_name = request.args.get('username')
    elif request.form.get('username') != None:
        isExistingData = True
        user_input_name = request.form.get('username')

    res = dict()
    if isExistingData:
        if user_input_name!=None and user_input_name!='':
            # Convert username to lower-case.
            user_input_name = user_input_name.lower()
            isUsernameDuplicated = is_username_existing(user_input_name)
            res['success'] = True
            if not isUsernameDuplicated:
                res['duplicated'] = False
                res['message'] = "Username '" + user_input_name + "' is not in use."
            else:
                res['duplicated'] = True
                res['message'] = "Username '" + user_input_name + "' is duplicated."
            res = make_response(jsonify(res), 200)
        else:
            res['success'] = False
            res['duplicated'] = True
            res['message'] = 'Error occurred when parsing request value.'
            res = make_response(jsonify(res), 400)
    else:
        res['success'] = False
        res['duplicated'] = True
        res['message'] = 'Error occurred when dealing with request.'
        res = make_response(jsonify(res), 500)
    return res

@app.errorhandler(400)
def invalid_data():
    return make_response(jsonify({'message': 'invalid_data'}), 400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
