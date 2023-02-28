from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from memoryjournalapi.models import Item, User

class ItemView(ViewSet):

    def retrieve(self, request, pk):
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def list(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(pk=request.data["user_id"])

        item = Item.objects.create(
            description=request.data["description"],
            image_url=request.data["image_url"],
            user=user
        )
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk):

        user = User.objects.get(pk=request.data["user_id"])

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

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'description', 'item_image', 'user')
        depth = 1
