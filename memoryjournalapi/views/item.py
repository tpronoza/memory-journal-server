from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
# from rest_framework.decorators import action
from memoryjournalapi.models import Item, User, List, List_Item
# from memoryjournalapi.serializers import ListItemSerializer

class ItemView(ViewSet):

    def retrieve(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
            # return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        user = User.objects.get(pk=request.data["user"])
        item = Item.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            image=request.data["image"],
            user=user,
        )
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.name=request.data["name"]
        item.description=request.data["description"]
        item.image=request.data["image"]
        # item.user=user
        item.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'image', 'user')
        depth = 2
