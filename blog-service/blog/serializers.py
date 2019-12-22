from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField()

    class Meta:
        model = Article
        fields = ('id', 'title', 'body', 'comment_to', 'author_id')
