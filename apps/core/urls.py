from django.urls import path, include
from loveshare.router import router
from . import viewset
# Routers provide an easy way of automatically determining the URL conf.
router.register(r'users', viewset.UserViewSet)


urlpatterns = [
    path('auth', include('rest_framework.urls')),
]