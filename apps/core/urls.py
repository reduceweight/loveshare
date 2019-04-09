from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from loveshare.router import router
from . import viewset
# Routers provide an easy way of automatically determining the URL conf.
router.register(r'users', viewset.UserViewSet )
# router.register(r'public', viewset.ImageViewSet)
img_upload = viewset.ImageViewSet.as_view({'post':'upload_img'})
file_upload = viewset.ImageViewSet.as_view({'post':'upload_file'})
urlpatterns = [
    path('auth', include('rest_framework.urls')),
    path('token/login', obtain_jwt_token),
    path('token/verify', verify_jwt_token),
    path('public/imgupload', img_upload),
    path('public/fileupload', file_upload),
]