from rest_framework import serializers
from share.models import *


# 会员中心
class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'


#文章
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'


#分类
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


#帖子
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
