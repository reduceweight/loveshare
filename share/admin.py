from django.contrib import admin
from .models import Member, Article, Document

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'mobile')
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'nickname')
    list_filter = ('sex',)

# 装饰器注册方法
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_date')
    list_per_page = 20
    ordering = ['pub_date']
    search_fields = ['title']

# 普通注册方法
admin.site.register(Member, MemberAdmin)

# 装饰器注册方法
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_per_page = 20
    search_fields = ['title']
