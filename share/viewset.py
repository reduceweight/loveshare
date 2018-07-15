from django_filters.rest_framework import DjangoFilterBackend

from share.models import *
from share.serializers import *
from rest_framework import viewsets,filters
from django_filters.rest_framework.backends import DjangoFilterBackend


class MemberViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_fields = ('name',)


#
#文章
class ArticleViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


#文章
class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


#
#文章
class PostViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.SearchFilter,DjangoFilterBackend)
    search_fields = ('title',)
    filter_fields = ('title',)

