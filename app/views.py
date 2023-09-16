from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    slider = Movie.objects.all()[0:3]
    latest_movie = Movie.objects.all()[3:]
    context = {
        'sliders':slider,
        'latest_movie':latest_movie
    }
    return render(request,'index.html',context=context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')