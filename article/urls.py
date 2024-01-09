from rest_framework.routers import DefaultRouter
from .views import ArticlesViewset, AuthorViewset
from django.urls import path, include


router = DefaultRouter()
router.register('articles', ArticlesViewset)
router.register('author', AuthorViewset)



urlpatterns = [
    path('', include(router.urls)),
]
