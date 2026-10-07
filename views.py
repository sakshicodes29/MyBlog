
from django.shortcuts import render, redirect
from .models import Post


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})


def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')

        Post.objects.create(
            title=title,
            author=author,
            content=content
        )

        return redirect('home')

    return render(request, 'blog/create_post.html')

