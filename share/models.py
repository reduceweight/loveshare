from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Member(models.Model):
    name = models.CharField(u'真实姓名',max_length=30)
    nickname = models.CharField(u'昵称',max_length=30)
    mobile = models.IntegerField(u'手机号')
    sex = models.IntegerField(choices=((0,'女'),(1,'男'),(-1, '暂时保密')), verbose_name='性别', default=-1)
    birthday = models.DateField(u'出生日期')
    email = models.EmailField(u'邮箱')

    class Meta:
        verbose_name = '会员'
        verbose_name_plural = '会员'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(u'标题',max_length=30)
    content = models.TextField(u'正文',max_length=300)
    photo = models.ImageField(verbose_name='图片', upload_to='uploads/', default='./frontend/static/images/indexView/house.png')
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title


class Document(models.Model):
    title = models.CharField(max_length=64, verbose_name='标题')
    content = RichTextUploadingField(null=True, blank=True, verbose_name='文档内容')

    class Meta:
        verbose_name = '文档'
        verbose_name_plural = '文档'

    def __str__(self):
        return self.title


# class Columns(models.Model):
#     name = models.CharField(max_length=36, verbose_name='名称')
#     explain = models.CharField(max_length=30, verbose_name='说明')
#     intro = models.TextField(default='', verbose_name='简介')
#
#     class Meta:
#         verbose_name = '栏目'
#         verbose_name_plural = '栏目'
#
#     def __str__(self):
#         return self.name


class Category(models.Model):
    title = models.CharField(max_length=96, unique=True, verbose_name='名称')
    explain = models.CharField(max_length=30, default='', verbose_name='说明')
    intro = models.TextField(default='', verbose_name='简介')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


class Post(models.Model):
    title = models.CharField(max_length=60, verbose_name='标题')
    content = models.TextField(max_length=300, verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    pub_date = models.DateTimeField(verbose_name='发布时间', default=None, blank=True, null=True, help_text='选择文章实际的发布时间，默认为文章创建时间。')
    weight = models.IntegerField(default=0, verbose_name='权重')
    like = models.IntegerField(default=0, verbose_name='点赞数量')
    page_view = models.IntegerField(default=0, verbose_name='浏览量')
    author = models.ForeignKey('auth.User', on_delete='', blank=True, null=True, verbose_name='作者')
    category = models.ManyToManyField(Category, default=None, verbose_name='分类')
    status = models.IntegerField(choices=((1, '已发布'), (0, '草稿')), default=1, verbose_name='状态')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    # def __str__(self):
    #     return self.title
    #
    # def get_url(self):
    #     return self.get_absolute_url()
    #
    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'pk': self.pk})
    #
    # def parent(self):
    #     return self.category
    #
    # def category_list(self):
    #     return ','.join([i.title for i in self.category.all()])