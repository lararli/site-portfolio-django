from django.test import TestCase, Client
from .models import Contact, contact_saved
from django.dispatch import Signal
from django.urls import reverse
from .views import contact_view
from django.test.utils import CaptureQueriesContext
from django.contrib.messages import get_messages
from django.contrib.messages.storage.fallback import FallbackStorage
from django.urls import resolve
from .forms import ContactForm


class ContactAppTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.contact_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com",
            "subject": "Test Subject",
            "message": "Test Message"
        }
    
    def test_contact_creation(self):
        contact = Contact.objects.create(**self.contact_data)
        self.assertEqual(contact.first_name, 'John')
        self.assertEqual(contact.last_name, 'Doe')
        self.assertEqual(contact.email, 'johndoe@example.com')
        self.assertEqual(contact.subject, 'Test Subject')
        self.assertEqual(contact.message, 'Test Message')
        self.assertEqual(contact.status, 'not_started')
        self.assertEqual(contact.resolution, '')

    def test_contact_str_representation(self):
        contact = Contact.objects.create(**self.contact_data)
        expected_str = 'John Doe'
        self.assertEqual(str(contact), expected_str)
    
    def test_contact_status_choices(self):
        contact = Contact.objects.create(**self.contact_data)
        choices = dict(Contact.STATUS_CHOICES)
        self.assertTrue(contact.status in choices)
    
    def test_contact_resolution_blank(self):
        contact = Contact.objects.create(**self.contact_data)
        self.assertEqual(contact.resolution, '')

    def test_contact_resolution_not_blank(self):
        contact = Contact.objects.create(**self.contact_data, resolution='Test Resolution')
        self.assertEqual(contact.resolution, 'Test Resolution')
    
    def test_contact_view_post(self):
        url = reverse('contact:contact')
        data = {
            'name': 'John Doe2',
            'email': 'johndoe@example.com',
            'message': 'Hello, Django!'
        }
        response = self.client.post(url, data)
        
        # Print captured queries
        self.assertEqual(response.status_code, 302)  # Check if the response is redirect
        
    
    
