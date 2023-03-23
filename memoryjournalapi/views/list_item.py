from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from memoryjournalapi.models import User, List_Item, List, Item
from memoryjournalapi.serializers import ListSerializer, ListItemSerializer

class ListItemView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single list_item"""
        try:
            list_item = List_Item.objects.get(pk=pk)
            serializer = ListItemSerializer(list_item)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        list_items = List_Item.objects.all()
        item_list = request.query_params.get('list', None)            
        # list_item = request.query_params.get('item', None)
        if item_list is not None:
            list_items.filter(list=item_list)
        
        serializer = ListItemSerializer(list_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        list = List.objects.get(pk=request.data['list_id'])
        item = Item.objects.get(pk=request.data['item_id'])

        list_item = List_Item.objects.create(
            list=list,
            item = item
        )
        serializer = ListItemSerializer(list_item)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a list_item"""
        item = Item.objects.get(pk=request.data["item"])
        list = List.objects.get(pk=request.data["list"])
        list_items = List_Item.objects.get(pk=pk)
        list_items.item = item
        list_items.list = list
        list_items.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        list_item = List_Item.objects.get(pk=pk)
        list_item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ListItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = List_Item
        fields = ('id', 'list', 'item')
        depth = 2
