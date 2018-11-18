from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    """文章类型"""
    name = models.CharField(max_length=10, verbose_name='文章类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类型信息'
        verbose_name_plural = verbose_name


class Article(models.Model):
    """文章信息，与用户一对多关系，与文章类型一对一关系"""
    EDITOR_CHOICES = (
        (0, "文本"),
        (1, 'markdown'),
        (2, 'UEditor'),
    )
    title = models.CharField(max_length=20, verbose_name='文章标题')
    type = models.CharField(max_length=2, choices=EDITOR_CHOICES, verbose_name=u'编辑类型')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='文章作者')
    category = models.ForeignKey(Category,related_name='articles',null=True, on_delete=models.SET_NULL, verbose_name='文章类型')
    desc = models.TextField(verbose_name='文章描述')
    content = models.TextField(verbose_name='文章正文')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    click_num = models.IntegerField(default=0, verbose_name='浏览量')
    love_num = models.IntegerField(default=0, verbose_name='点赞量')
    image = models.ImageField(upload_to='article/%y/%m/%d', verbose_name='文章图片', null=True, max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章信息'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    comment_content = models.CharField(max_length=200, verbose_name='文章评论')
    comment_art = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='所属文章')
    comment_man = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='评论人')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.comment_content

    class Meta:
        verbose_name = '评论信息'
        verbose_name_plural = verbose_name
