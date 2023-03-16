from rest_framework import serializers
from memoryjournalapi.models import List, List_Item

class ListItemSerializer(serializers.ModelSerializer):
    """words"""
    class Meta:
        model = List_Item
        depth = 1
        fields = ('list', 'item')
        
class ListSerializer(serializers.ModelSerializer):
    """JSON serializer for Item"""
    myList = ListItemSerializer(many=True)
    class Meta:
        model = List
        fields = ('id', 'user', 'category', 'title', 'image_url', 'description', 'myList')
