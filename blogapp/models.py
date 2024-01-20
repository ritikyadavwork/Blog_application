from django.db import models
from model_utils.models import TimeStampedModel


class Post(TimeStampedModel):
    title = models.CharField(max_length=200, null=True)
    blog = models.TextField()
    photos = models.ImageField(upload_to='Upload_images/')

    def __str__(self):
        return self.title


class category(TimeStampedModel):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Comment(TimeStampedModel):
    Author = models.CharField(max_length=225)
    comment = models.TextField()
    title = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return self.Author
