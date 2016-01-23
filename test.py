# coding: utf-8
from app import app
from flask import jsonify
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        # s = u'这个字怎么念？'

        response = tester.post('/test', data={'test': 'kyle'})
        print response
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
