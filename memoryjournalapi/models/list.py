
from django.db import models
from memoryjournalapi.models import Category, User

class List(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image_url = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    # status = models.BooleanField()

    @property
    def myList(self):
      myList = []
      for list in self.user_listitem.all():
          myList.append(list)
      return myList
  
    # @property
    # def item_list(self):
    #     return self.__item_list

    # @item_list.setter
    # def item_list(self, value):
    #     self.__item_list=value
