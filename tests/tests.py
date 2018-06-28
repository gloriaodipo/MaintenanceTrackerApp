from ..app.views import app
import json

from .base import BaseClass

SIGNUP_URL = '/api/v1/user/signup'
LOGIN_URL = '/api/v1/user/login'
REQUEST_URL = '/api/v1/requests'

class TestUserCase(BaseClass):
    """This class represents the user test cases."""

    def test_can_successfully_signup_a_user(self):
        """Test API can successfully register a new user"""
        response = self.client.post(
            SIGNUP_URL, data = json.dumps(self.user_data), content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Successfully registered")
        self.assertEqual(response.status_code, 201)

    def test_cannot_signup_twice(self):
        """Test API cannot register a user twice(POST request)"""
        self.client.post(
            SIGNUP_URL,data = json.dumps(self.user_data), content_type = 'application/json')
        response2 = self.client.post(SIGNUP_URL, 
            data = json.dumps(self.user_data), content_type = 'application/json')
        result = json.loads(response2.data.decode())
        self.assertEqual(result["message"], "User already exists")
        self.assertEqual(response2.status_code, 203)

    def test_wrong_signup(self):
        """Test API cannot successfully register a new user if any field is left blank(POST request)"""
        response = self.client.post(SIGNUP_URL,
            data = json.dumps({'username':'caren','department':'',
            'email':'caren@gmail.com', 'password': 'passw'}) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "All fields required")
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        """Test API can successfully log in registered users using username and password (POST request)"""
        response = self.client.post(LOGIN_URL,
             data=json.dumps({'username':'carenakinyi', 'password':'passw'}),
            content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "You are successfully logged in")
        self.assertEqual(response.status_code, 200)

    def test_cannot_login_without_username(self):
        """Test API cannot login a user when username is blank (POST request)"""
        response = self.client.post(LOGIN_URL, 
            data=json.dumps({'username':'', 'password':'passw'}), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'please enter username')
        self.assertEqual(response.status_code, 400)

    def test_cannot_login_without_password(self):
        """Test API cannot login a user without a password"""
        response = self.client.post(LOGIN_URL, data=json.dumps({'username':"caren", 'password':""}),
             content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'please enter password')
        self.assertEqual(response.status_code, 400)

    def test_wrong_login(self):
        """Test API cannot authenticate login when wrong password is used (POST request)"""
        response = self.client.post(LOGIN_URL, 
            data=json.dumps({'username':'carenakinyi', 'password':'www'}),
            content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Wrong password.')
        self.assertEqual(response.status_code, 401)

    def test_login_nonexistent_user(self):
        """Test API cannot authenticate login when user is nonexistent (POST request)"""
        response = self.client.post(LOGIN_URL,
            data=json.dumps({'username':'glo', 'password':'passw'}), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'User unavailable')
        self.assertEqual(response.status_code, 404)    

class TestRequestsCase(BaseClass):
    """This is the class for request test cases"""

    def test_add_request(self):
        """Test API can post a request (POST request)"""
        response = self.client.post(REQUEST_URL, 
            data = json.dumps(self.request_data) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "request made")
        self.assertEqual(response.status_code, 201) 

    def test_get_all_requestss(self):
        """Test API can get all requests (GET request)"""
        response = self.client.get(REQUEST_URL,
             data = json.dumps(self.request_data) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
