from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.shortcuts import render, redirect
# from .forms import BlogPostForm
from django.shortcuts import render, redirect
from .models import contactform
from .forms import contact  

def home(request):
    return render(request, "a.html")

def seo_view(request):
    return render(request, "seo.html")

def digital_view(request):
    return render(request, "digital.html")

def data_view(request):
    return render(request, "data.html")

def web_view(request):
    return render(request, "web.html")

def app_view(request):
    return render(request, "app.html")

def product_view(request):
    return render(request, "product.html")

def blog_list(request):
    posts = BlogPost.objects.filter(published=True).order_by('-created_at')
    return render(request, 'digital/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'digital/blog_detail.html', {'post': post})

# You can remove blog_home or just redirect to blog_list:
def home(request):
    latest_blogs = BlogPost.objects.filter(published=True).order_by('-created_at')[:4]  # show latest 3
    return render(request, "a.html", {'posts': latest_blogs})
def success(request):
    return render(request, 'success.html')





