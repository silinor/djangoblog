from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField()
    tags = models.ManyToManyField('Tag')
    user = models.ForeignKey(User, null=True)


class Tag(models.Model):
    title = models.CharField(max_length=255)


class Comment(models.Model):
    post = models.ForeignKey('Post', null=True)
    user = models.ForeignKey(User, null=True)
    comment = models.TextField()