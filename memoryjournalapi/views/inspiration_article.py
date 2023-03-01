from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from memoryjournalapi.models import Inspiration_Article, User

class InspirationArticleView(ViewSet):

    def retrieve(self, request, pk):
        inspiration_article = Inspiration_Article.objects.get(pk=pk)
        serializer = InspirationArticleSerializer(inspiration_article)
        return Response(serializer.data)

    def list(self, request):
        inspiration_articles = Inspiration_Article.objects.all()
        serializer = InspirationArticleSerializer(inspiration_articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(pk=request.data["user"])

        inspiration_article = Inspiration_Article.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            item_image=request.data["item_image"],
            user=user
        )
        serializer = InspirationArticleSerializer(inspiration_article)
        return Response(serializer.data)

    def update(self, request, pk):

        user = User.objects.get(pk=request.data["user"])

        inspiration_article = Inspiration_Article.objects.get(pk=pk)
        inspiration_article.title=request.data["title"]
        inspiration_article.description=request.data["description"]
        inspiration_article.item_image=request.data["item_image"]
        # inspiration_article.user=user
        inspiration_article.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        inspiration_article = Inspiration_Article.objects.get(pk=pk)
        inspiration_article.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class InspirationArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inspiration_Article
        fields = ('id', 'title', 'description', 'item_image', 'user')
        depth = 1
