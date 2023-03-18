from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from memoryjournalapi.models import List, User, Item, List_Item
# from memoryjournalapi.serializers import ListSerializer, ListItemSerializer

class ListView(ViewSet):

    def retrieve(self, request, pk):
        try:
            list = List.objects.get(pk=pk)
            items = Item.objects.filter(joined_items__list_id=list)
            list.items.set(items)
            serializer = ListSerializer(list, context={'list': list})
            return Response(serializer.data)
        except List.DoesNotExist as ex:
            return HttpResponseServerError(ex)
            # return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        lists = List.objects.all()
        item = request.query_params.get('item', None)
        if item is not None:
            items = items.filter(item_id=item)
            item = request.query_params.get('item_id', None)
        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        user = User.objects.get(pk=request.data["user"])
        # category = Category.objects.get(pk=request.data["category"])
        list = List.objects.create(
            name=request.data["name"],
            image=request.data["image"],
            description=request.data["description"],
            # status=request.data["status"],
            user=user,
            # category=category
        )
        serializer = ListSerializer(list)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests"""
        list = List.objects.get(pk=pk)
        list.name = request.data["name"]
        list.image = request.data["image"]
        list.description = request.data["description"]
        list.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle Delete requests for a list"""
        list = List.objects.get(pk=pk)
        list.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = List_Item
        fields = ('id',)
class ItemSerializer(serializers.ModelSerializer):
    """Handle GET request for single list"""
    joined_items = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = (
          'id', 
          'name',
          'description',
          'image', 
          'user',
          'joined_items')

    def get_joined_items(self, obj):
        """Handle GET request for single list"""
        list = self.context.get('list')
        listitems = obj.joined_items.filter(list=list)
        serializer = ListItemSerializer(listitems, many=True)
        
        return serializer.data
class ListSerializer(serializers.ModelSerializer):
    items=ItemSerializer(many=True)
    class Meta:
        model = List
        fields = ('id', 'name', 'image', 'description', 'user', 'items')
        depth = 2

    # @action(methods=['get'], detail=True)
    # def get(self, request, pk):
    #     """post for get list"""
        
    #     item = Item.objects.get(pk=request.data["item_id"])
    #     list = List.objects.get(pk=pk)
    #     list_item = List_Item.objects.get(
    #         item=item,
    #         list=list
    #     )
    #     return Response({'message': 'List Added'}, status=status.HTTP_201_CREATED)
    
    # @action(methods=['post'], detail=True)
    # def watch(self, request, pk):
    #     """post for view list"""
        
    #     item = Item.objects.get(pk=request.data["item_id"])
    #     list = List.objects.get(pk=pk)
    #     list_item = List_Item.objects.create(
    #         item=item,
    #         list=list
    #     )
    #     return Response({'message': 'List Added'}, status=status.HTTP_201_CREATED)
    
    # @action(methods=['delete'], detail=True)
    # def drop(self, request, pk):
    #     """delete from list"""
        
    #     item = Item.objects.get(pk=request.data["item_id"])
    #     list = List.objects.get(pk=pk)
    #     list_item = List_Item.objects.filter(
    #         item=item,
    #         list=list
    #     )
    #     list_item.delete()
    #     return Response({'message': 'List Dropped'}, status=status.HTTP_204_NO_CONTENT)

# class ListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = List
#         fields = ('id', 'name', 'image', 'description', 'user', 'category')
#         depth = 1
