from django.test import TestCase 
from .models import Project, Profile, Review

# Create your tests here.
class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.project = Project(id=1, image='path/to/image', title='test',description='Quote time', url='path/to/project', user=self.user)
        self.user = User.objects.create_user(username='testuser', password='ran5678')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))
