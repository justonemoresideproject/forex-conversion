from unittest import TestCase

from flask.wrappers import Response
from app import app
from flask import request

class FlaskTests(TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Makes sure the front page sets up correctly"""

        with self.client:
            response = self.client.get('/')
            self.assertIsNone(response.get['to'])
            self.assertIsNone(response.get['from'])
            self.assertIsNone(response.get['amount'])


    def test_valid_amount(self):
        with self.client:
            response = self.client.get('/get-currency?from=USD&to=EUR&amount=10')
            self.assertEqual(response.get['to'], 'EUR')
            self.assertEqual(response.get['from'], 'USD')
            self.assertEqual(response.get['amount'], '10')
            self.assertEqual('USD', 'USD', '10'), 10.0

