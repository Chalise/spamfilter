#!/usr/bin/env python3

from flask import Flask
from flask_restful import Resource, Api, request

import random

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Spam(Resource):
    def post(self):
        # Placeholder functionality
        # Just returns true/false randomly
        answer = bool(random.getrandbits(1))
        message = request.json["email"]

        return {"spam": answer}

api.add_resource(HelloWorld, '/', '/hello')
api.add_resource(Spam, '/spam')

if __name__ == '__main__':
    app.run(debug=True)
