from django.shortcuts import render
from .models import Movie
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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


def userlogin(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:

            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            context = {"error":"Invalid Username or Password"}
            return render(request,'login.html',context)

    return render(request,'login.html')



@login_required(login_url='login')
def administration(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request,'dashboard.html',context=context)

@login_required(login_url='login')
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))