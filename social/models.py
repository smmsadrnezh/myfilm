from django.db import models
from myfilm.models import Movie
# Create your models here.
class Post:
    post_id = models.IntegerField(primary_key=True)
    title = models.CharField()
    # username = models.ForeignKey(User)
    # movie = models.ForeignKey(Movie)
    body = models.TextField()
    time = models.TimeField()