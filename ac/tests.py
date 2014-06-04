"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.contrib.auth.models import User

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
        john = User.objects.create_user(username='john',
                                     first_name='john',
                                     last_name='doe',
                                     email='john@example.com',
                                     password='j0h62@dfig')
        john.save()

        users = User.objects.all()
        self.assertEqual(users.count(), 1) # Number of users.

        john_as_coordinator = Coordinator.objects.create(user=john)
        john_as_coordinator.save()
        self.assertEqual(john_as_coordinator.user.username, "john")
