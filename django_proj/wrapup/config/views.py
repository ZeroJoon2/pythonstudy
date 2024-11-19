from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from post.models import *

def index(request):
    return render(request, 'index.html')
