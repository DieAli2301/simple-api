import unittest
import json
from app import app

class UserRegistrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_register_user(self):
        user = {
            'username': 'testuser',
            'email': 'testuser@example.com'
        }
        response = self.app.post('/register', data=json.dumps(user), content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'User registered successfully!')

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
