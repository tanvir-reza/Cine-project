from django.shortcuts import render
from .models import Movie,Info
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    slider = Movie.objects.all()[0:3]
    latest_movie = Movie.objects.all()
    context = {
        'sliders':slider,
        'latest_movie':latest_movie
    }
    return render(request,'index.html',context=context)

def moviedetails(request,id):
    movie = Movie.objects.get(pk=id)
    context = {
        'movie':movie
    }
    return render(request,'movie-details.html',context=context)

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
def siteInfo(request):
    info = Info.objects.all().first()
    context = {
        'siteinfo':info
    }
    return render(request,'info.html',context=context)


@login_required(login_url='login')
def Addmovie(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard'))
    context = {
        'title':'Add Movie',
        'form':form
    }
    return render(request,'modify.html',context=context)


@login_required(login_url='login')
def Editmovie(request,id):
    movie = Movie.objects.get(pk=id)
    form = MovieForm(instance=movie)
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES,instance=movie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard'))
    context = {
        'title':'Edit Movie',
        'form':form
    }
    return render(request,'modify.html',context=context)

@login_required(login_url='login')
def Deletemovie(request,id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return HttpResponseRedirect(reverse('dashboard'))

@login_required(login_url='login')
def updateInfo(request):
    info = Info.objects.get(pk=1)
    form = InfoForm(instance=info)
    if request.method == 'POST':
        form = InfoForm(request.POST,request.FILES,instance=info)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard'))
    context = {
        'title':'Edit Info',
        'form':form
    }
    return render(request,'modify.html',context=context)


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


