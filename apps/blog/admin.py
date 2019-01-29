from django.contrib import admin

# Register your models here.
from . models import ArticlePost

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'owner', 'updated')

admin.site.register(ArticlePost,BlogAdmin)