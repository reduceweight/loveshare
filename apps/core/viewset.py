from rest_framework import generics, serializers, viewsets,mixins
from core.rest import UserSerializer, User, ImgModel, ImgSerializer
from core.rest import FileModel, FileSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ImageViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ImgModel.objects.all()
    def get_queryset(self):
        if self.action == 'upload_img':
            return ImgModel.objects.all()
        elif self.action == 'upload_file':
            return FileModel.objects.all()
        return ImgModel.objects.all()

    def get_serializer_class(self):
        if self.action == 'upload_img':
            pass
        elif self.action == 'upload_file':
            return FileSerializer
        return ImgSerializer

    @action(detail=False, methods=['post'], url_path='upload_img', name='upload image')
    def upload_img(self, request, pk=None):
        return self.create(request)

    @action(detail=False, methods=['post'], url_path='upload_file', name='upload file')
    def upload_file(self, request, pk=None):
        return self.create(request)
