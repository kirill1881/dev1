from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
