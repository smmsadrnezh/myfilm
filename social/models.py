from django.db import models
from myfilm.models import Movie
from accounts.models import User
# Create your models here.
class Post:
    post_id = models.IntegerField(primary_key=True)
    title = models.CharField()
    #username = models.ForeignKey(accounts.User)
    #movie = models.ForeignKey(myfilm.Movie)
    body = models.TextField()
    time = models.TimeField()