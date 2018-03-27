# coding:utf-8
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from .models import Member, Article

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

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
        # members = Member.objects.all().values('id','name')
        # response['list'] = list(members)
        members = Member.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", members))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])

            if user:
                login(request, user)
                request.session['user_id'] = user.id
                return HttpResponse("登录成功，欢迎你来到！")
            else:
                return HttpResponse("登录失败，你的用户名或密码不正确!")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "login.html", {"form": login_form})

def user_logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse("你已经退出登录!")


def get_Article(request):
    title = request.GET.get('title')

    result_list = filter(lambda x: x.startwith(title))
