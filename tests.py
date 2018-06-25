from app.views import app
import json

from base import BaseClass

class UserTestCase(BaseClass):
    """This class represents the user test cases."""

    def test_signup(self):
        """Test API can successfully register a new user (POST request)"""
        response = self.client.post('/api/v1/user/signup', data = json.dumps(self.user_data), content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Successfully registered")
        self.assertEqual(response.status_code, 201)

    def test_wrong_signup(self):
        """Test API cannot successfully register a new user if any field is left blank(POST request)"""
        response = self.client.post('/api/v1/user/signup', data = json.dumps({'username':'caren','department':'','email':'caren@gmail.com', 'password': 'passw'}) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "All fields required")
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        """Test API can successfully log in registered users using username and password (POST request)"""
        response = self.client.post('/api/v1/user/login', data=json.dumps({'username':'carenakinyi', 'password':'passw'}), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "You are successfully logged in")
        self.assertEqual(response.status_code, 200)

    def test_wrong_login(self):
        """Test API cannot authenticate login when wrong password is used or no password supplied (POST request)"""
        response = self.client.post('/api/v1/user/login', data=json.dumps({'username':'carenakinyi', 'password':'www'}), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Wrong password.')
        self.assertEqual(response.status_code, 401)

    def test_login_nonexistent_user(self):
        """Test API cannot authenticate login when user is nonexistent (POST request)"""
        response = self.client.post('/api/v1/user/login', data=json.dumps({'username':'glo', 'password':'passw'}), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'User unavailable')
        self.assertEqual(response.status_code, 404)    

class RequestsTestCase(BaseClass):
    """This is the class for request test cases"""

    def test_add_request(self):
        """Test API can post a request (POST request)"""
        response = self.client.post('/api/v1/requests', data = json.dumps(self.request_data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "request made")
        self.assertEqual(response.status_code, 201) 

    def test_get_all_requestss(self):
        """Test API can get all requests (GET request)"""
        response = self.client.get('/api/v1/requests', data = json.dumps(self.request_data) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200)