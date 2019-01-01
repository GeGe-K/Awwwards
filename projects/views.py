from django.shortcuts import render, redirect
from rest_framework.response import Response


# Create your views here.
def index(request):
    '''
    Function that renders the homepage 
    '''

    return render (request, 'index.html')