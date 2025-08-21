from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(TimeStampedModel):
    title = models.CharField(max_length=200, null=True)
    blog = RichTextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='Upload_images/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Category(TimeStampedModel):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Comment(TimeStampedModel):
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.comment[:20]


class UserProfile(TimeStampedModel):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    mobile_number = models.CharField(max_length=225)
    address = models.TextField()
    photos = models.ImageField(upload_to='user_profile/')

    def __str__(self):
        return self.name


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes', null=True)


