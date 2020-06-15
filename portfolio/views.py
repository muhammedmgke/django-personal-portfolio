from django.http import HttpResponse
from django.shortcuts import render
from .models import Project
from blog.models import Blog


# Create your views here.
def home(request):
    projects = Project.objects.all()
    blogs = Blog.objects.order_by('-date')
    return render(request, 'portfolio/home.html', {'projects': projects, 'blogs': blogs})


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})
