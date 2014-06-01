"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.http import HttpRequest

from ac.views import index

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(3 * 5, 15)


class HomePageTest(TestCase):
    """Test aakashlabs.org home page"""
    def test_index(self):
        request = HttpRequest()
        response = index(request)
        self.assertTrue(response.content.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Aakashlabs</title>', response.content)
        #FIXME:Should be endswith
        self.assertTrue(response.content.find('</html>'))
