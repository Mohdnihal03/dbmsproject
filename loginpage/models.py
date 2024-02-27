from django.db import models

class User(models.Model):
    email = models.CharField(unique=True)
    password = models.CharField(max_length=128)  