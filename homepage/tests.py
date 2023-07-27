from django.test import TestCase
from .models import Profile, URLs
from django.urls import reverse
from django.shortcuts import get_object_or_404

class ModelTests(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(name='John Doe', bio='Test bio')
        # Assuming you have a URL pattern defined for the 'homepage' view
        # self.url = reverse('homepage')  # Replace 'homepage' with the actual URL name

    def test_profile_manager_get_profile(self):
        profile = Profile.objects.get_profile()
        self.assertIsNotNone(profile)
        self.assertIsInstance(profile, Profile)

    def test_profile_manager_get_or_create(self):
        profile, created = Profile.objects.get_or_create(pk=1)
        self.assertTrue(created)
        self.assertEqual(profile.pk, 1)
        self.assertIsInstance(profile, Profile)

    def test_urls_model_str(self):
        url = URLs.objects.create(name='Example', url='http://example.com', image='example.jpg')
        self.assertEqual(str(url), 'Example')
