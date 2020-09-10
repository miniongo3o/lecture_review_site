from django.db import models

class Nick(models.Model):
    nick_nickname = models.CharField(max_length=100)

    def __str__(self):
        return self.nick_nickname