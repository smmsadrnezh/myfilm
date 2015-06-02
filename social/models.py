from django.db import models
# Create your models here.

class Post:
    post_id = models.IntegerField(primary_key=True)
    title = models.CharField()
    username = models.ForeignKey('accounts.User')
    movie = models.ForeignKey('myfilm.Movie')
    body = models.TextField()
    created_time = models.TimeField()

class Comment:
    username = models.ForeignKey('accounts.User',primary_key=True)
    post_id = models.ForeignKey('Post', primary_key=True)
    body = models.TextField()
    time = models.TimeField()

class Like:
    username = models.ForeignKey('accounts.User',primary_key=True)
    post_id = models.ForeignKey('social.Post',primary_key=True)
    time = models.TimeField()

class Movie_Rating:
    username = models.ForeignKey('accounts.User',primary_key=True)
    movie = models.ForeignKey('myfilm.Movie',primary_key=True)
    rate = models.IntegerField()
