from marshmallow import Schema, fields
import random

class User():

    def __init__(self, username, department, email, password):
        self.user_id = random.randint(1,100)
        self.username = username
        self.department = department
        self.email = email
        self.password = password 

class User_Schema(Schema):
    user_id = fields.Int()
    username = fields.Str()
    department = fields.Str()
    email = fields.Email()
    password = fields.Str()
    admin = fields.Boolean()

class Requests():
    def __init__(self,req_id, request_title, description):
        self.req_id = req_id
        self.request_title = request_title
        self.description = description

class Requests_Schema(Schema):
    req_id = fields.Int()
    request_title = fields.Str()
    description= fields.Str()