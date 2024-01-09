from django.shortcuts import render
from rest_framework import viewsets
from .models import Article, Author
from .serializers import ArticleSerailizer, AuthorSerializer
# Create your views here.


class ArticlesViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerailizer

class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
