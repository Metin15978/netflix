from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def movies(request):
    filmler = Movie.objects.all()
    context = {
        'filmler': filmler
    }
    return render(request,'browse-index.html',context)

def video(request):
    video = Movie.objects.all()
    context = {
        'video': video
    }
    return render(request,'video.html',context)