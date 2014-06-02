"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string

from ac.views import index, about

from ac.models import Coordinator


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
        self.assertTrue(response.content.strip().endswith('</html>'))


    def test_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)        
        index_html = render_to_string('index.html')
        self.assertEqual(response.content, index_html)


    def test_root_url_resolve_to_index(self):
        root_url = resolve('/')
        self.assertEquals(root_url.func, index)
        


class AcModelTest(TestCase):
    """Check models in 'ac' app."""

    def test_coordinator_model(self):
        coordinator = Coordinator()
        coordinator.user = "admin"
