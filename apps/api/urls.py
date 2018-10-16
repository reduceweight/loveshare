from django.urls import path, include
from loveshare.router import router
from . import viewsets
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
router.register(r'users', viewsets.UserViewSet)
router.register(r'groups', viewsets.GroupViewSet)


urlpatterns = [
    path('auth', include('rest_framework.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-verify/', verify_jwt_token),
]