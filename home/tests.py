from django.test import RequestFactory,TestCase
from home.models import Document
from django.contrib.auth.models import AnonymousUser, User
from .views import index

class DocumentTestCase(TestCase):
    def setUp(self):
        self.document = Document.objects.create()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@gekko.fr', password='top_secret')


    def test_document_can_save(self):
        self.document.save()
        retrieveDocument = Document.objects.all().first()
        self.assertEqual(retrieveDocument,self.document)

    def test_home_index_anonymous(self):
        # Create an instance of a GET request.
        request = self.factory.get('/home/')
        request.user = AnonymousUser()
        response = index(request)
        self.assertEqual(response.status_code, 302)
    
    def test_home_index_connected(self):
        # Create an instance of a GET request.
        request = self.factory.get('/home/')
        request.user = self.user
        response = index(request)
        self.assertEqual(response.status_code, 200)