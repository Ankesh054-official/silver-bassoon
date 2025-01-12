from flask import Flask, jsonify, request
from flask_restful import Resource, Api

class Generate(Resource):

    def __init__(self):
        self.__response = {
            'choices': [
                {'message':{
                        'content':""
                    }
                }
            ]
        }

    def post(self):
        data = request.json
        if not data:
            return jsonify({"error": "Invalid or missing JSON data"}), 400
        self.__prompt = data.get('prompt')

        self.__response['choices'][0]['message']['content'] = f"{self.__prompt}"

        return jsonify(self.__response)