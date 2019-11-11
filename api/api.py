#!/usr/bin/env python3

from flask import Flask
from flask_restful import Resource, Api, request

from backend import prepare_data
from backend import spamfilter

import random

app = Flask(__name__)
api = Api(app)
classifier = None

print("Training the classifier. This may take some time...")
classifier = spamfilter.get_classifier()
print("Classifier trained!")

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Spam(Resource):
    def post(self):
        message = request.json.get("email")
        answer = classifier.classify(spamfilter.dictionary(prepare_data.prepare_data(message)))
        return {"spam": answer}

api.add_resource(HelloWorld, '/', '/hello')
api.add_resource(Spam, '/spam')

if __name__ == '__main__':
    app.run(debug=True)
