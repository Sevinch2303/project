from django.shortcuts import render

def home_view(request):
    return render(request, 'blog/home.html')

def about_view(request):
    return render(request, 'blog/about.html')

def blog_view(request):
    return render(request, 'blog/blog.html')

def contact_view(request):
    return render(request, 'blog/contact.html')
