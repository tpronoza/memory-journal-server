from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from memoryjournalapi.models import List, User, Category

class ListView(ViewSet):

    def retrieve(self, request, pk):
        list = List.objects.get(pk=pk)
        serializer = ListSerializer(list)
        return Response(serializer.data)

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
            status=request.data["status"],
            user=user,
            category=category
        )
        serializer = ListSerializer(list)
        return Response(serializer.data)

    def update(self, request, pk):

        user = User.objects.get(pk=request.data["user"])
        category = Category.objects.get(pk=request.data["category"])

        list = List.objects.get(pk=pk)
        list.category=category
        list.title=request.data["title"]
        list.image_url=request.data["image_url"]
        list.description=request.data["description"]
        list.status=request.data["status"]
        list.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        list = List.objects.get(pk=pk)
        list.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = ('id', 'title', 'image_url', 'description', 'status', 'user', 'category')
        depth = 1
