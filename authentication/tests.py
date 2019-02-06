from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from .views import index, logout_view

class AuthenticationTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@gekko.fr', password='top_secret')

    def test_root_index_anonymous(self):
        # Create an instance of a GET request.
        request = self.factory.get('/')
        request.user = AnonymousUser()
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_root_index_connected(self):
        # Create an instance of a GET request.
        request = self.factory.get('/')
        request.user = self.user
        response = index(request)
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        # Create an instance of a GET request.
        request = self.factory.get('/auth/logout')
        request.user = self.user
        response = index(request)
        self.assertEqual(response.status_code, 302)
    