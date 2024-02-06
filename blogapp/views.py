from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Category, Comment, UserProfile
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required


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


def update_View(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    context = {
        'comment': comment
    }
    return render(request, 'update_comment.html', context)


def update_comment_View(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    # if request.user  != comment.Author:
    #     return render(request, 'unauthorized_access.html')
    if request.method == 'POST':
        author = request.POST.get('author')
        comment_text = request.POST.get('msg')
        comment.Author = author
        comment.comment = comment_text
        comment.save()
        return redirect(reverse('blogapp:fullDetail', kwargs={'post_id': comment.post.id}))
    return render(request, 'update_comment.html', {'comment': comment})


def delete_post_view(request, delete_id):
    post_delete = Post.objects.get(id=delete_id)
    if request.user == request.user.username:
        post_delete.delete()
    else:
        return render(request, 'unauthorized_access.html')


def uploadProfile_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile')
        address = request.POST.get('address')
        photos = request.FILES.get('images')
        instance = UserProfile.objects.create(name=name, mobile_number=mobile_number, address=address, photos=photos)
        instance.save()
        return redirect('/profile-view')
    return render(request, 'profile.html')


def profile_view(request):
    data = UserProfile.objects.get()
    context = {
        'final_data': data
    }
    return render(request, 'profile_view.html', context)
