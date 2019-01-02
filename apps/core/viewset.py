from rest_framework import routers, serializers, viewsets
from core.rest import UserSerializer, User

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer