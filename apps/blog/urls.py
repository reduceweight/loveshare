from django.conf.urls import url, include
from loveshare.router import router
from . import viewset

router.register(r'blog', viewset.ArticleViewSet)
router.register(r'category', viewset.CategoryViewSet)
urlpatterns = [

]