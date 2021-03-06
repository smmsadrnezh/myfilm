from django.db import models
from django.contrib.auth.models import User, UserManager


class CustomUser(User):
    """Consider that this class inherit django user class.
    user class fields:  username, email, password, is_staff, is_active, date_joined and much more.
    More help on this: http://scottbarnham.com/blog/2008/08/21/extending-the-django-user-model-with-inheritance """

    image_path = models.ImageField(upload_to='users', null=True, default='default.jpg')
    birth_date = models.DateField(null=True)

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()


class Follow(models.Model):
    follower = models.ForeignKey('CustomUser', related_name='+')
    following = models.ForeignKey('CustomUser', related_name='+')
    time = models.TimeField()

    class Meta:
        unique_together = (("follower", "following"),)

    def __str__(self):
        return "%s %s" % (self.follower, self.following)