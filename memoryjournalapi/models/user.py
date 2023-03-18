from django.db import models

class User(models.Model):

    uid = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
