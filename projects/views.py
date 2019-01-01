from django.shortcuts import render, redirect
from rest_framework.response import Response


# Create your views here.
def index(request):
    '''
    Function that renders the homepage 
    '''
    if User.objects.filter(username=request.user.username).exists():
        user = User.objects.get(username=request.user)
        if not Profile.objects.filter(user=request.user).exists():
            Profile.objects.create(user=user)
    projects = Project.object.order_by('-posted_on')
    return render (request, 'index.html',{"projects":projects})