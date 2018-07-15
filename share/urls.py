from django.urls import path
from share import views
from share import viewset
from loveshare.api import router

router.register(r'member', viewset.MemberViewSet)
router.register(r'article', viewset.ArticleViewSet)
router.register(r'post', viewset.PostViewSet)
router.register(r'category', viewset.CategoryViewSet)




urlpatterns = [
    path('add_member', views.add_member, ),
    path('show_members', views.show_members, ),
    path('getCategoryList', views.category_list, ),
    path('getArticleList', views.article_list, ),
]