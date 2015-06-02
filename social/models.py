from django.db import models


class Post:
    title = models.CharField()
    username = models.ForeignKey('accounts.User')
    movie = models.ForeignKey('myfilm.Movie')
    body = models.TextField()
    created_time = models.TimeField()

    def __str__(self):
        return "%s" % (self.title)


class Comment:
    username = models.ForeignKey('accounts.User', primary_key=True)
    post_id = models.ForeignKey('Post', primary_key=True)
    body = models.TextField()
    time = models.TimeField()

    def __str__(self):
        return "%s" % (self.body)


class Like:
    username = models.ForeignKey('accounts.User', primary_key=True)
    post_id = models.ForeignKey('Post', primary_key=True)
    time = models.TimeField()

    def __str__(self):
        return "%s" % (self.time)


class Movie_Rating:
    username = models.ForeignKey('accounts.User', primary_key=True)
    movie = models.ForeignKey('myfilm.Movie', primary_key=True)
    rate = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.movie, self.rate)