from django.db import models


class ChatMessage(models.Model):
    from_user = models.ForeignKey('accounts.CustomUser', related_name='+')
    to_user = models.ForeignKey('accounts.CustomUser', related_name='+')
    time = models.TimeField()
    message = models.TextField()

    class Meta:
        unique_together = (("time", "from_user", "to_user"),)

    def __str__(self):
        return "%s %s %s" % (self.time, self.from_user, self.to_user)