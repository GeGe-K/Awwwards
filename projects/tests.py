from django.test import TestCase 
from .models import Project, Profile, Review

# Create your tests here.
class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.project = 