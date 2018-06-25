from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json
import random

from .models import User, Requests, Requests_Schema

app = Flask(__name__)
api = Api(app)

users = []
requests = []

class UserSignupAPI(Resource):
    def post(self):
        user = request.get_json()
        username = user['username']
        department = user['department']
        email = user['email']
        password = user['password']

        u = User(
            username=username,
            department=department,
            email=email,
            password=password
            )

        if not user['username'] or not user['department'] or not user['email'] \
                or not user['password']:
            result = jsonify({'message': 'All fields required'}) 
            result.status_code = 400
            return result

        else:
            users.append(u)
            result = jsonify({'message': 'Successfully registered'})
            result.status_code = 201
            return result

class UserLoginAPI(Resource):

    def post(self):
        access = request.get_json()
        username = access['username']
        password = access['password']

        for user in users:
            if username == user.username:
                if password == user.password:
                    result = jsonify({"message": "You are successfully logged in"})
                    result.status_code = 200
                    return result
                else:
                    result =jsonify({'message': 'Wrong password.'})
                    result.status_code = 401
                    return result
            else:
                result = jsonify({"message": "User unavailable"})
                result.status_code = 404
                return result
                       
class RequestsAPI(Resource):
    def post(self):
        req = request.get_json()
        r = Requests(req_id=req.get('req_id'), request_title=req.get('request_title'),
        description=req.get('description'))

        requests.append(r)

        result = jsonify({"message": "request made"})
        result.status_code = 201
        return result

    def get(self):
        req = Requests_Schema(many = True)
        request_items = req.dump(requests)

        result = jsonify(request_items.data)
        result.status_code = 200
        return result

api.add_resource(UserSignupAPI, '/api/v1/user/signup')
api.add_resource(UserLoginAPI, '/api/v1/user/login')
api.add_resource(RequestsAPI, '/api/v1/requests')

if __name__ == '__main__':
    app.run(debug=True)