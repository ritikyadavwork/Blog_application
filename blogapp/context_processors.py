from .models import Post, Category, Comment, UserProfile


def custom_context(request):
    context={}
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user_profile=request.user)
            context['image'] = user_profile
        except:
            pass
    # print("user profile", user_profile)

    # # images = UserProfile.objects.first()
    return context


# get(user=request.user)
