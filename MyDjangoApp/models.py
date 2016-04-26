from __future__ import unicode_literals

from django.db import models

# Create your models here. However, we could not configure for mongoDB in settings.py
class MySampleModel(models.Model):
    name = models.CharField(max_length=20)
    age  = models.CharField(max_length=10)
    street = models.CharField(max_length=30)
    #tags = ListField()
    #comments = ListField()
