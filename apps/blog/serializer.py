from rest_framework import serializers
from . import models
from api.serializers import UserSerializer

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.StringRelatedField(source='user.username')
    # 获取当前登录的用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    # def create(self, validated_data):
    #     # 除了用户，其他数据可以从validated_data这个字典中获取
    #     # 注意，users在这里是放在上下文中的request，而不是直接的request
    #     user = self.context['request'].user
    #     validated_data['user'] = user
    #     return models.Article.objects.create(**validated_data)

    class Meta:
        model = models.Article
        # fields = '__all__'
        read_only_fields = ('add_time','click_num','love_num')
        exclude = ('is_delete',)

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # articles = ArticleSerializer(many=True, read_only=True)
    class Meta:
        model = models.Category
        fields = '__all__'
        read_only_fields = ('add_time','articles')