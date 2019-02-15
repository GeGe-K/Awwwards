from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    link = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.title

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True, blank=True)
    bio = 
    contacts = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user.username
    
class Review(models.Model):
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    average = models.IntegerField(default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_review(self):
        self.save()
    
    def delete_review(self):
        self.delete()

    def __str__(self):
        return self.project.title
