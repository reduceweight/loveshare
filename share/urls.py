from django.urls import path
from share import views

urlpatterns = [
    path('add_member', views.add_member, ),
    path('show_members', views.show_members, ),
    path('getCategoryList', views.category_list, ),
    path('getArticleList', views.article_list, ),
]