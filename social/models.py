from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    username = models.ForeignKey(User)
    movie = models.ForeignKey('myfilm.Movie')
    body = models.TextField()
    created_time = models.TimeField()

    def __str__(self):
        return "%s" % self.title


class Comment(models.Model):
    username = models.ForeignKey(User)
    post = models.ForeignKey('Post')
    body = models.TextField()
    time = models.TimeField()

    class Meta:
        unique_together = (("username", "post"),)

    def __str__(self):
        return "%s" % self.body


class Like(models.Model):
    username = models.ForeignKey(User)
    post = models.ForeignKey('Post')
    time = models.TimeField()

    class Meta:
        unique_together = (("username", "post"),)

    def __str__(self):
        return "%s" % self.time


class MovieRating(models.Model):
    username = models.ForeignKey(User)
    movie = models.ForeignKey('myfilm.Movie')
    rate = models.IntegerField()

    class Meta:
        unique_together = (("username", "movie"),)

    def __str__(self):
        return "%s %s" % (self.movie, self.rate)