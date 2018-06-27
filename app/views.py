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
        elif u.email in [i.email for i in users]:
            result = jsonify({"message": "User already exists"})
            result.status_code = 203
            return result
        elif u.username in [i.username for i in users]:
            result = jsonify({"message": "User already exists"})
            result.status_code = 203
            return result
        
        users.append(u)

        return {"message":"Successfully registered"},201 

class UserLoginAPI(Resource):

    def post(self):
        access = request.get_json()
        username = access['username']
        password = access['password']

        if username == "":
            return {"message":"please enter username"}, 400
        elif password == "":
            return {"message":"please enter password"} ,400   
        else:
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
                
                result = jsonify({"message": "User unavailable"})
                result.status_code = 404
                return result
                       
class RequestsAPI(Resource):
    def post(self):
        req = request.get_json()
        req_id = req['req_id']
        request_title = req['request_title']
        description = req['description']

        r = Requests(
            req_id=req_id,
            request_title=request_title,
            description=description
            )

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
