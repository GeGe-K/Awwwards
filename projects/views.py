from django.shortcuts import render, redirect
from .models import Project, Profile,Review
from .forms import UpdateProfile, UploadProject,ReviewForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer, ProfileSerializer

# Create your views here.
def index(request):
    '''  

    Function that renders the homepage 
    '''
    if User.objects.filter(username=request.user.username).exists():
        user = User.objects.get(username=request.user)
        if not Profile.objects.filter(user=request.user).exists():
            Profile.objects.create(user=user)
    project= Project.objects.order_by('-posted_on')
    print(project)
    return render (request, 'index.html',{'projects':project})

def profile(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    projects = Project.objects.filter(user = user)
    return render(request, 'profile.html', {'profile':profile, 'projects':projects})

# @login_required(login_url='/accounts/login/')
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

# @login_required(login_url='/accounts/login/')
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
    return render(request, 'upload.html',{'form':form})

def project(request,id):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        project = Project.objects.get(id=id)
        reviews = Review.objects.filter(project=project)
        design = reviews.aggregate(Avg('design'))['design__avg']
        usability = reviews.aggregate(Avg('usability'))['usability__avg']
        content = reviews.aggregate(Avg('content'))['content__avg']
        average = reviews.aggregate(Avg('average'))['average__avg']
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.average = (review.design + review.usability + review.content) / 3
                review.project = project
                review.user = user
                review.save()
            return redirect('index', id)
        else:
            form = ReviewForm()
    return render(request, 'project.html', {'project': project, 'reviews':reviews, 'form':form, 'design':design, 'usability':usability, 'content':content, 'average':average})

def search_project(request):
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get('project')
        projects = Project.objects.filter(title__icontains=search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'projects':projects, 'message':message})
    else:
        message = "You haven't seaeched for any project"
        return render (request, 'search.html',{"message":message})

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
