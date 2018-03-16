# coding:utf-8
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Member, Article
from django.core import serializers
import json

def home(request):
    article_list = Article.objects.all()
    return render(request, 'home.html', {
        'article': article_list
    })

@require_http_methods(["GET"])
def add_member(request):
    response = {}
    try:
        member = Member(name = request.GET.get('name'))
        member.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_members(request):
    response = {}
    try:
        members = Member.objects.all().values('id','name')
        response['list']  = list(members)
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)