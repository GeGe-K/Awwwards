from rest_framework import serializers
from .models import Project, Profile

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ('title', 'description', 'image', 'link', 'user', 'posted_on')

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('user', 'profile_pic', 'bio', 'contacts')