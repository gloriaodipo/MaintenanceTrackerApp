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
            return {'message': 'All fields required'}, 400
            
        elif u.email in [i.email for i in users]:
            return {"message": "User already exists"}, 203
    
        elif u.username in [i.username for i in users]:
            return {"message": "User already exists"}, 203

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
                        return {"message": "You are successfully logged in"}, 200

                    else:
                        return {'message': 'Wrong password.'}, 401
                        
                return {"message": "User unavailable"}, 404


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

        return {"message": "request made"}, 201
        
    def get(self):
        req = Requests_Schema(many = True)
        request_items = req.dump(requests)

        return {"request": request_items }, 200
        
api.add_resource(UserSignupAPI, '/api/v1/user/signup')
api.add_resource(UserLoginAPI, '/api/v1/user/login')
api.add_resource(RequestsAPI, '/api/v1/requests')

if __name__ == '__main__':
    app.run(debug=True)
