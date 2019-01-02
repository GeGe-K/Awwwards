from django.shortcuts import render, redirect
from .models import Project, Profile
from .forms import UpdateProfile, UploadProject
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
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
    projects = Project.objects.order_by('-posted_on')
    return render (request, 'index.html',{"projects":projects})

def profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    projects = Project.objects.filter(user = user)
    return render(request, 'profile.html', {'profile':profile, 'projects':projects})

@login_required(login_url='/accounts/login/')
def update_profile(request, id):
    if request.method =="POST":
        profile = Profile.objects.get(id=id)
        form = UpdateProfile(request.POST or None,request.FILES or None, instance=profile)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return redirect('profile', username=request.user)
    else:
        form = UpdateProfile()
    return render(request, 'update_profile.html', {'form': form})

@login_required(login_url='/accounts/login/')
def upload_project(request):
    if request.method == 'POST':
        form = UploadProject(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('index')
    else:
        form = UploadProject()
    return redirect(request, 'upload.html',{'form':form})

