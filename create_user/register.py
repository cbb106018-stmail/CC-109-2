from flask import Flask, request, json, jsonify, make_response
from flasgger import Swagger, SwaggerView, Schema, swag_from
from sender import pass_on


app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'APIDOCS for create_user',
    'openapi': '3.0.2',
    'uiversion': '3',
    'optional_fields': ['components']
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
    "url_prefix": "/api/create_user"
}

template = {
  "swagger": "3.0",
  "info": {
    "title": "APIDOCS for create user service",
    "description": "User create API",
    "contact": {
      "responsibleOrganization": "CBB106018",
      "responsibleDeveloper": "CBB106018",
      "email": "cbb106018@nptu.edu.tw",
      "url": None,
    },
    "termsOfService": None,
    "version": "1.0.0"
  },
  "host": "104.46.235.6",
  "basePath": "/api",
  "schemes": [
    "http",
    "https"
  ],
  "components": {
      "schemas":    {}
    }
}

swagger = Swagger(app, config=swagger_config, template=template)

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
        if 'userrole' in jsonobj:
            userrole = json.dumps(jsonobj['userrole']).replace("\"", "")
        else:
            userrole = None
    elif request.values.get('username')!=None and request.values.get('password')!=None:
        isExistingData = True
        username = request.values.get('username')
        password = request.values.get('password')
        userrole = request.values.get('userrole')

    res = dict()
    if isExistingData:
        # Convert username to lower case here.
        username = username.lower()
        if userrole == None:
            userrole = 'user'
        user_info['username'] = username
        user_info['password'] = password
        user_info['userrole'] = userrole
        isRequestCompleted = pass_on(user_info)

        if isRequestCompleted == True:
            res['success'] = True
            res['message'] = 'User create request successfully sent to the queue: ' + username + '.'
            res = make_response(jsonify(res), 200)
        else:
            res['success'] = False
            res['message'] = 'Error occurred when processing request.'
            res = make_response(jsonify(res), 400)
    else:
        res['success'] = False
        res['message'] = 'Error occurred when parsing data.'
        res = make_response(jsonify(res), 500)
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
