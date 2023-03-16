from django.db import models
from .list import List
from .item import Item

class List_Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="user_listitem")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
