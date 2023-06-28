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

    # def test_profile_view(self):
    #     response = self.client.get(self.url)

    #     self.assertEqual(response.status_code, 200)  # Assert that the response status code is 200 (OK)
    #     self.assertTemplateUsed(response, 'homepage.html')  # Assert that the correct template is used

    #     # Retrieve the profile from the database
    #     profile = get_object_or_404(Profile, id=self.profile.id)
    #     self.assertEqual(response.context['profile'], profile)  # Assert that the correct profile is passed to the template

    #     # Assert the profile attributes
    #     self.assertEqual(profile.name, 'John Doe')
    #     self.assertEqual(profile.bio, 'Test bio')