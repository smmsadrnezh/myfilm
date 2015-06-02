from django.db import models

# Create your models here.
class Chat_Message:
    from_user = models.ForeignKey('accounts.User',primary_key=True)
    to_user = models.ForeignKey('accounts.User',primary_key=True)
    time = models.IntegerField(primary_key=True)
    message = models.TextField()