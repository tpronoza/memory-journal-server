from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
# from rest_framework.decorators import action
from memoryjournalapi.models import Item, User, List, List_Item
from memoryjournalapi.serializers import ListItemSerializer

class ItemView(ViewSet):

    def retrieve(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        except Item.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(pk=request.data["user"])
        item = Item.objects.create(
            description=request.data["description"],
            image_url=request.data["image_url"],
            user=user
        )
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk):

        user = User.objects.get(pk=request.data["user"])

        item = Item.objects.get(pk=pk)
        item.description=request.data["description"]
        item.image_url=request.data["image_url"]
        # item.user=user
        item.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    # @action(methods=['post'], detail=True)
    # def watch(self, request, pk):
    #     """post for watching anime"""
        
    #     list = List.objects.get(pk=request.data["list_id"])
    #     item = Item.objects.get(pk=pk)
    #     list_item = List_Item.objects.create(
    #         list=list,
    #         item=item
    #     )
    #     return Response({'message': 'List Added'}, status=status.HTTP_201_CREATED)
    
    # @action(methods=['delete'], detail=True)
    # def drop(self, request, pk):
    #     """delete from list"""
        
    #     list = List.objects.get(pk=request.data["list_id"])
    #     item = Item.objects.get(pk=pk)
    #     list_item = List_Item.objects.filter(
    #         list=list,
    #         item=item
    #     )
    #     list_item.delete()
    #     return Response({'message': 'List Dropped'}, status=status.HTTP_204_NO_CONTENT)
    

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'description', 'image_url', 'user')
        # depth = 1
