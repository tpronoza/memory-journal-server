from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from memoryjournalapi.models import User, List_Item, List, Item

class ListItemView(ViewSet):

    def list(self, request):

        list_items = List_Item.objects.all()
        # list_user = request.query_params.get('user', None)
        # if list_user is not None:
        #     list_items.filter(user=list_user)
            
        list_item = request.query_params.get('item', None)
        if list_item is not None:
            games = games.filter(list_item_id=list_item)
        
        serializer = ListItemSerializer(list_items, many=True)
        return Response(serializer.data)

    def create(self, request):

        list = List.objects.get(pk=request.data['list'])
        item = Item.objects.get(pk=request.data['item'])

        list_item = List_Item.objects.create(
            list=list,
            item = item
        )
        serializer = ListItemSerializer(list_item)
        return Response(serializer.data)

    def destroy(self, request, pk):
        list_item = List_Item.objects.get(pk=pk)
        list_item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ListItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = List_Item
        fields = ('id', 'list', 'item')
        depth = 1
