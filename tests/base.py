import unittest
import json
from ..app.views import app
from ..app.views import users, requests

class BaseClass(unittest.TestCase):
    """This is the base class for test cases."""

    def setUp(self):
        """Initialize app and define test variables"""
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.user_data = {
                    "username":"carenakinyi", 
                    "department":"finance",
                    "email":"caren@gmail.com",
                    "password":"passw"
                    }
        self.request_data = {
                    "req_id": 4,
                    "request_title": "Faulty chair",
                    "description": "blablablaaaaaaaaaa"
                    }

    def tearDown(self):
        """ Clear anything that has been saved. """
        users = []
        requests = []                 