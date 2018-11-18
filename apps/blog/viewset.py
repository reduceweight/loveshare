from rest_framework import permissions, viewsets, renderers
from rest_framework.decorators import (
    permission_classes, detail_route
)
from .serializer import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from api.permissions import IsOwnerOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = ( IsOwnerOrReadOnly,)