from django.db import models

class User:
    username = models.CharField(primary_key=True)
    email = models.EmailField()
    real_name = models.CharField()
    image_path = models.FilePathField()
    birth_date = models.DateField()
    password = models.CharField()

    def __str__(self):
        return "%s" % (self.username)

class Follow:
    follower = models.ForeignKey('User',primary_key=True)
    following = models.ForeignKey('User',primary_key=True)
    time = models.TimeField()

    def __str__(self):
        return "%s %s" % (self.follower,self.following)