from django.contrib import admin
from .models import Member, Article, Document, Category, Post

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

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_per_page = 20
    search_fields = ['title']

# @admin.register(Columns)
# class ColumnsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'slug')
#     list_display_links = ('id', 'name', 'slug')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','explain')
    list_display_links = ('id', 'title')
    list_per_page = 20


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category_list')
    list_display_links = ('id', 'title', 'author')
    list_per_page = 20
    ordering = ['pub_date']