from django.db import models
from core.rest import BaseModel

# Create your models here.
# 博客文章数据模型
class ArticlePost(BaseModel):
    EDITOR_CHOICES = (
        (1, 'markdown'),
        (2, 'UEditor'),
    )
    title = models.CharField(max_length=20, verbose_name='文章标题')
    desc = models.TextField(verbose_name='文章描述')
    type = models.CharField(max_length=2,default=1, choices=EDITOR_CHOICES, verbose_name='编辑类型')
    content = models.TextField(verbose_name='文章正文')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'
