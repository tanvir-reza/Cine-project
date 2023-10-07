from django.shortcuts import render
from .models import Movie,Info,Category,professional
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
    latest_movie = Movie.objects.all().order_by('-id')[0:6]
    pro = professional.objects.all().first()
    context = {
        'sliders':slider,
        'latest_movie':latest_movie,
        'pro':pro
    }
    return render(request,'index.html',context=context)

def moviedetails(request,id):
    movie = Movie.objects.get(pk=id)
    context = {
        'movie':movie
    }
    return render(request,'movie-details.html',context=context)

def category(request,category):
    movies = Movie.objects.filter(genre__name=category)
    context = {
        'movies':movies,
        'category':category
    }
    return render(request,'category.html',context=context)

def about(request):
    info = Info.objects.all().first()
    context = {
        'info':info
    }
    return render(request,'about.html',context)

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
def category_admin(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request,'category-admin.html',context=context)

@login_required(login_url='login')
def category_add(request):
    form = CategoryForm()
    if request.method == 'POST':
        print(request.POST)
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard'))
    context = {
        'title':'Add Category',
        'form':form
    }
    return render(request,'modify.html',context=context)

def category_edit(request,id):
    category = Category.objects.get(pk=id)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES,instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('category-admin'))
    context = {
        'title':'Edit Category',
        'form':form
    }
    return render(request,'modify.html',context=context)

def category_delete(request,id):
    category = Category.objects.get(pk=id)
    category.delete()
    return HttpResponseRedirect(reverse('category-admin'))


@login_required(login_url='login')
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def custom_404(request, exception):
    return render(request, '404.html', status=404)


