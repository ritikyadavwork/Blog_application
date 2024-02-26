from .models import Post, Category, Comment, UserProfile


def custom_context(request):
    images = UserProfile.objects.get()
    # images = UserProfile.objects.first()
    return {'image': images}

# get(user=request.user)
