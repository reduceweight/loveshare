from loveshare.router import router
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class BaseSerializer(serializers.HyperlinkedModelSerializer):
    # 这样就可以直接获取到当前用户
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault())