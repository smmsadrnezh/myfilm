from django.db import models

class Chat_Message:
    from_user = models.ForeignKey('accounts.User',primary_key=True)
    to_user = models.ForeignKey('accounts.User',primary_key=True)
    time = models.TimeField(primary_key=True)
    message = models.TextField()

    def __str__(self):
        return "%s %s %s" % (self.time,self.from_user,self.to_user)