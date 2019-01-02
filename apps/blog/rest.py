from rest_framework import viewsets
from .models import ArticlePost
from core.rest import UserSerializer, BaseSerializer


class PostSerializer(BaseSerializer):
    author = UserSerializer(source='owner',read_only=True)
    
    class Meta:
        model = ArticlePost
        fields = '__all__'

class PostViewSet(viewsets.ModelViewSet):
    queryset = ArticlePost.objects.all()
    serializer_class = PostSerializer