from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Category, Project
from .views import index
from datetime import date

class IndexViewTest(TestCase):
    def setUp(self):
        # Create test categories for testing the view
        self.category1 = Category.objects.create(name="Category 1")
        self.category2 = Category.objects.create(name="Category 2")

        # Create test projects for testing the view
        self.test_project1 = Project.objects.create(
            project_name="Test Project 45",
            description="This is a test project 45",
            date=date(2023, 7, 27)
            # Add other required fields as per your Project model
        )
        self.test_project1.tags.add(self.category1)

        self.test_project2 = Project.objects.create(
            project_name="Test Project 45",
            description="This is a test project 45",
            date=date(2023, 7, 27)
            # Add other required fields as per your Project model
        )
        self.test_project2.tags.add(self.category2)

        # URL to the index view
        self.url = reverse('index')  # Assuming you have set up the URL pattern with the name 'index'

    def test_index_view(self):
        # Test the index view with a GET request
        response = self.client.get(self.url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used for rendering the response
        self.assertTemplateUsed(response, 'projects.html')

        # Check if the projects are present in the context
        self.assertIn('projects', response.context)

        # Check if the correct number of projects is displayed in the rendered HTML
        self.assertContains(response, self.test_project1.project_name)
        self.assertContains(response, self.test_project2.project_name)

        # Check if the project categories are displayed in the rendered HTML
        self.assertContains(response, self.category1.name)
        self.assertContains(response, self.category2.name)

    def test_index_view_empty(self):
        # Test the index view when there are no projects in the database
        Project.objects.all().delete()  # Delete all projects from the database

        response = self.client.get(self.url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used for rendering the response
        self.assertTemplateUsed(response, 'projects.html')

        # Check if no projects are present in the context
        # self.assertNotIn('projects', response.context)

        # Check if a specific message is displayed in the rendered HTML when there are no projects
        # self.assertContains(response, "No projects found.")

