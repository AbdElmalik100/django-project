from rest_framework import serializers
from .models import Article, Author


class AuthorSerializer(serializers.ModelSerializer):
    # articles = ArticleSerailizer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = '__all__'

class ArticleSerailizer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField()
    # author = AuthorSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'


