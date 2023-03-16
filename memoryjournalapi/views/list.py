from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from memoryjournalapi.models import List, User, Category, Item, List_Item
from memoryjournalapi.serializers import ListSerializer, ListItemSerializer

class ListView(ViewSet):

    def retrieve(self, request, pk):
        try:
            list = List.objects.get(pk=pk)
            serializer = ListSerializer(list)
            return Response(serializer.data)
        except List.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        lists = List.objects.all()
        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(pk=request.data["user"])
        category = Category.objects.get(pk=request.data["category"])

        list = List.objects.create(
            title=request.data["title"],
            image_url=request.data["image_url"],
            description=request.data["description"],
            # status=request.data["status"],
            user=user,
            category=category
        )
        serializer = ListSerializer(list)
        return Response(serializer.data)

    # def update(self, request, pk):

    #     user = User.objects.get(pk=request.data["user"])
    #     category = Category.objects.get(pk=request.data["category"])

    #     list = List.objects.get(pk=pk)
    #     list.category=category
    #     list.title=request.data["title"]
    #     list.image_url=request.data["image_url"]
    #     list.description=request.data["description"]
    #     # list.status=request.data["status"]
    #     list.save()

    #     return Response(None, status=status.HTTP_204_NO_CONTENT)

    # def destroy(self, request, pk):
    #     list = List.objects.get(pk=pk)
    #     list.delete()
    #     return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=True)
    def watch(self, request, pk):
        """post for view list"""
        
        item = Item.objects.get(pk=request.data["item_id"])
        list = List.objects.get(pk=pk)
        list_item = List_Item.objects.create(
            item=item,
            list=list
        )
        return Response({'message': 'List Added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def drop(self, request, pk):
        """delete from list"""
        
        item = Item.objects.get(pk=request.data["item_id"])
        list = List.objects.get(pk=pk)
        list_item = List_Item.objects.filter(
            item=item,
            list=list
        )
        list_item.delete()
        return Response({'message': 'List Dropped'}, status=status.HTTP_204_NO_CONTENT)

# class ListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = List
#         fields = ('id', 'title', 'image_url', 'description', 'user', 'category')
#         depth = 1
