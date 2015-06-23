from django.db import models
import django.utils.timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    username = models.ForeignKey('accounts.CustomUser')
    movie = models.ForeignKey('myfilm.Movie')
    body = models.TextField()
    created_time = models.TimeField()

    def __str__(self):
        return "%s" % self.title


class Comment(models.Model):
    username = models.ForeignKey('accounts.CustomUser')
    post = models.ForeignKey('Post')
    body = models.TextField()
    time = models.TimeField()
    title = models.TextField()

    class Meta:
        unique_together = (("username", "post", "time"),)

    def __str__(self):
        return "%s" % self.body


class Like(models.Model):
    username = models.ForeignKey('accounts.CustomUser')
    post = models.ForeignKey('Post')
    time = models.TimeField()

    class Meta:
        unique_together = (("username", "post"),)

    def __str__(self):
        return "%s" % self.time


class MovieRating(models.Model):
    username = models.ForeignKey('accounts.CustomUser')
    movie = models.ForeignKey('myfilm.Movie')
    rate = models.IntegerField()

    class Meta:
        unique_together = (("username", "movie"),)

    def __str__(self):
        return "%s %s" % (self.movie, self.rate)


class Notification(models.Model):
    text = models.CharField(max_length=100)
    time = models.TimeField(default=django.utils.timezone.now)
    username = models.ForeignKey('accounts.CustomUser')
    url = models.URLField(max_length=50)

    def __str__(self):
        return "notification: %s username: %s" % (self.text, self.username)