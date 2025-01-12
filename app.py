from flask import Flask, jsonify, request
from flask_restful import Resource, Api

from resources import Generate as genai

app = Flask(__name__)

api = Api(app)

api.add_resource(genai, '/genai')

if __name__ == '__main__':
    app.run(debug = True)