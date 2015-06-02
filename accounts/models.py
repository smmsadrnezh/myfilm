from django.db import models


# Create your models here.
class User:
    username = models.CharField(primary_key=True)
    email = models.EmailField()
    real_name = models.CharField()
    image_path = models.FilePathField()
    birth_date = models.DateField()
    password = models.CharField()

class Follow:
    follower = models.ForeignKey('User',primary_key=True)
    following = models.ForeignKey('User',primary_key=True)