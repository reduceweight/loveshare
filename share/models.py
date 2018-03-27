from django.db import models
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

