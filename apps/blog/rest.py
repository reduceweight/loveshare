from rest_framework import serializers, viewsets
from .models import ArticlePost

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticlePost
        fields = '__all__'

class PostViewSet(viewsets.ModelViewSet):
    queryset = ArticlePost.objects.all()
    serializer_class = PostSerializer