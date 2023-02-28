
from django.db import models
from .user import User

class Inspiration_Article(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    item_image = models.CharField(max_length=100)
