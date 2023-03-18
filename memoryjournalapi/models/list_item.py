from django.db import models
from .list import List
from .item import Item

class List_Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="joined_items")

    class Meta:
        unique_together = ('item', 'list')
