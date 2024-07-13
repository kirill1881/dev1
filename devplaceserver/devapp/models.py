from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    time = models.CharField(max_length=255)


class Manager(models.Model):
    name = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255)
    username = models.CharField(max_length=255)


