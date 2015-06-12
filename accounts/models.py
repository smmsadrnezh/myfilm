from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Consider that this class inherit django user class.
    user class fields:  username, email, password, is_staff, is_active, date_joined and much more.
    More help on this: http://scottbarnham.com/blog/2008/08/21/extending-the-django-user-model-with-inheritance """
    user = models.ForeignKey(User, unique=True, related_name='profile')
    image_path = models.FilePathField(null=True, default="default.jpg")
    birth_date = models.DateField(null=True)


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='+')
    following = models.ForeignKey(User, related_name='+')
    time = models.TimeField()

    class Meta:
        unique_together = (("follower", "following"),)

    def __str__(self):
        return "%s %s" % (self.follower, self.following)