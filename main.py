from flask import Flask, request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app = Flask(__name__)
app.json_encoder = LazyJSONEncoder

swagger_template = dict(
info = {
    'title': LazyString(lambda: 'This is a Swagger Flask Test'),
    'version': LazyString(lambda: '0.1'),
    'description': LazyString(lambda: 'This document depicts a      sample Swagger UI document and implements Hello World functionality after executing GET.'),
    },
    host = LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'hello_world',
            "route": '/hello_world.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

swagger = Swagger(app, template=swagger_template,             
                  config=swagger_config)

@swag_from("hello_world.yml", methods=['GET'])
@app.route("/")
def hello_world():
    return "Hello World!!!"

if __name__ == '__main__':
    app.run('0.0.0.0',port=8080)