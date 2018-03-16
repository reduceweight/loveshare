from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(u'真实姓名',max_length=30)
    nickname = models.CharField(u'昵称',max_length=30)
    mobile = models.IntegerField(u'手机号')
    sex = models.IntegerField(u'性别')
    birthday = models.DateField(u'出生日期')
    email = models.EmailField(u'邮箱')

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(u'标题',max_length=30)
    content = models.TextField(u'正文',max_length=300)
    photo = models.ImageField(verbose_name='图片', upload_to='frontend/static/uploads/', default='./frontend/static/images/common/cate_banner.jpg')
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)

    def __str__(self):
        return self.title