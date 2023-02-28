
from django.db import models
from .user import User

class Item(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
