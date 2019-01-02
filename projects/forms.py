from django import forms
from .models import Project, Profile, Review

class UpdateProfile(forms.ModelForm):
    
    class Meta:
        model = Profile
        exclude = ['user']

class UploadProject(forms.ModelForm):
    
    class Meta:
        model = Project
        exclude = ['user','posted_on']

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ['project', 'user']