from django.db import models
from django.contrib.auth.models import User

class Expend(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    def __str__(self):
        return self.text


class Income(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()


