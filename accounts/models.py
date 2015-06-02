from django.db import models
from django.contrib.auth.models import User, UserManager

class CustomUser(User):
    """Consider that this class inherit django user class.
    user class fields:  username, email, password, is_staff, is_active, date_joined and much more.
    More help on this: http://scottbarnham.com/blog/2008/08/21/extending-the-django-user-model-with-inheritance """

    real_name = models.CharField(max_length=100)
    image_path = models.FilePathField()
    birth_date = models.DateField()

class Follow:
    follower = models.ForeignKey('User',primary_key=True)
    following = models.ForeignKey('User',primary_key=True)
    time = models.TimeField()

    def __str__(self):
        return "%s %s" % (self.follower,self.following)