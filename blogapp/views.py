from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Category, Comment
from django.core.paginator import Paginator
from django.db.models import Q


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
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        instance = Post.objects.create(title=title, blog=blog, photos=photos, category=category)
        instance.save()
        return redirect('/blog-list')
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'postblog.html', context)


def blogList_view(request):
    search_post = request.GET.get('search')
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post) | Q(category__name__icontains=search_post))
    else:
        posts = Post.objects.all().order_by('created')
    paginator = Paginator(posts, 3)
    page_num = request.GET.get('page')
    final_data = paginator.get_page(page_num)
    context = {
        "post": final_data
    }
    return render(request, 'blog_list.html', context)


def blogDetail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        author = request.POST.get('author')
        comment_text = request.POST.get('msg')
        comment = Comment.objects.create(
            Author=author,
            comment=comment_text,
            post=post,
        )
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        'object': post,
        'comments': comments,
    }
    return render(request, 'blog_detail.html', context)


