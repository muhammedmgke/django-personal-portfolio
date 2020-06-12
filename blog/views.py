from django.shortcuts import render


# Create your views here.
from blog.models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:3]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})
