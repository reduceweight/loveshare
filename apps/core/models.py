from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    # 创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now,null=True)
    # 更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)
    # 创建人
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True)

    class Meta:
        abstract = True
