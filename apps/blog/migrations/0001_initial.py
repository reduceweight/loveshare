# Generated by Django 2.0.7 on 2018-11-18 07:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='文章标题')),
                ('type', models.CharField(choices=[(0, '文本'), (1, 'markdown'), (2, 'UEditor')], max_length=2, verbose_name='编辑类型')),
                ('desc', models.TextField(verbose_name='文章描述')),
                ('content', models.TextField(verbose_name='文章正文')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('click_num', models.IntegerField(default=0, verbose_name='浏览量')),
                ('love_num', models.IntegerField(default=0, verbose_name='点赞量')),
                ('image', models.ImageField(max_length=200, null=True, upload_to='article/%y/%m/%d', verbose_name='文章图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '文章信息',
                'verbose_name_plural': '文章信息',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='文章类型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '类型信息',
                'verbose_name_plural': '类型信息',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=200, verbose_name='文章评论')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('comment_art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='所属文章')),
                ('comment_man', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论人')),
            ],
            options={
                'verbose_name': '评论信息',
                'verbose_name_plural': '评论信息',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Category', verbose_name='文章类型'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='文章作者'),
        ),
    ]