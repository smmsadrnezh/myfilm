from django.db import models


# Create your models here.
class User(models.model):
    username = models.CharField(primary_key=True)
    email = models.EmailField()
    real_name = models.CharField()
    image_path = models.FilePathField()
    birth_date = models.DateField()
    password = models.CharField()


