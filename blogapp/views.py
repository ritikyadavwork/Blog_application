from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post


def homeView(request):
    return render(request, 'home.html')


def login(request):
    print(request.user.user_name)
    return render(request, 'login.html')


def postBlog_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        blog = request.POST.get('blog')
        photos = request.FILES.get('images')
        instance = Post.objects.create(title=title, blog=blog, photos=photos)
        instance.save()
        return redirect('/blog-list')
    return render(request, 'postblog.html')


def blogList_view(request):
    posts = Post.objects.all()
    context = {
        "post": posts
    }
    return render(request, 'blog_list.html', context)


def blogDetail_view(request, post_id):
    data = get_object_or_404(Post, id=post_id)
    context = {
        'object': data
    }
    return render(request, 'blog_detail.html', context)
