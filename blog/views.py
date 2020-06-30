from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Junyao's Blogs")

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {}
    context ['blog_obj'] = blog
    return render(request, "blog_detail.html", context)

def blog_list(request):
    blogs = Blog.objects.all()
    context = {}
    context ['blogs'] = blogs
    return render(request, "blog_list.html", context)
