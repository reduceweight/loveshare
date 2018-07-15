# Generated by Django 2.1 on 2018-03-14 03:32

from django.db import migrations, models
from django.contrib.auth.models import User

def initAdmin(apps, schema_editor):
    # User = get_user_model()
    if User.objects.all().filter(username='admin').count() < 1 :
        User.objects.create_superuser('admin', 'admin@qq.com', 'admin')



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunPython(initAdmin),

        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='真实姓名')),
                ('nickname', models.CharField(max_length=30, verbose_name='昵称')),
                ('mobile', models.IntegerField(verbose_name='手机号')),
                ('sex', models.IntegerField(verbose_name='性别')),
                ('birthday', models.DateField(verbose_name='出生日期')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
            ],
        ),
    ]
