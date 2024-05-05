import pandas as pd
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from world.authentication import EmailBackend
from . import authentication
from .models import Standing, Team, Player, Match, Statistic
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# excel数据读取
excel_data1 = pd.read_excel('数据话英超.xls')


# Create your views here.
# 第一个位子是视图函数的request参数，第二个参数位是html文件路径

def user_list(request):
    return render(request, "user_list.html")


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        # 获取参数
        user_name = request.POST.get('username', '')
        pwd = request.POST.get('password', '')
        email = request.POST.get('email', '')
        # 用户已存在
        if User.objects.filter(email=email):
            return render(request, 'register.html', {'tip': '用户已存在'})
        # 用户不存在
        else:
            user = User.objects.create_user(
                username=user_name,
                password=pwd,
                email=email,
                is_staff=1,
                is_active=1,
                is_superuser=0
            )
            return render(request, 'register.html', {'tip': '注册成功'})
    else:
        return render(request, 'register.html', {'tip': '无效的请求'})


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', )
    elif request.method == 'POST':
        # 获取参数
        email = request.POST.get('email', '')
        pwd = request.POST.get('password', '')
        # 用户已存在
        if User.objects.filter(email=email):
            # 使用内置方法验证
            user = authenticate(request, username=email, password=pwd)
            # 验证通过
            if user:
                # 用户已激活
                if user.is_active:
                    return redirect('/home/')
                # 未激活
                else:
                    return render(request, 'login.html', {'tip': '用户未激活'})
            # 验证失败
            else:
                return render(request, 'login.html', {'tip': '用户认证失败'})
        # 用户不存在
        else:
            return render(request, 'login.html', {'tip': '用户不存在！'})


def get_standing(request):
    if request.method == 'GET':
        teams = Standing.objects.all()
        return render(request, "home.html", {"teams": teams})
    elif request.method == 'POST':
        search_filter = {}
        search_data = request.POST.get('search')
        if search_data:
            search_filter['name__icontains'] = search_data
            teams = Standing.objects.filter(**search_filter).order_by('-points')
            return render(request, "home.html", {"teams": teams})


def get_team_details(request, team_id):
    img = Standing.objects.get(teamid=team_id)
    teams = Team.objects.get(teamid=team_id)
    matches = Match.objects.filter(
        Q(hostteamid=teams.shortname) | Q(guestteamid=teams.shortname)
    )
    players = Player.objects.filter(teamname=teams.name).order_by('-prize')
    return render(request, "demo.html", {
        "img": img,
        "Team": teams,
        "matches": matches,
        "players": players,
        "team_id": team_id
    })


def get_player_details(request, player_id):
    player_data = Player.objects.get(playerid=player_id)
    behavior_data = Statistic.objects.get(playerid=player_id)
    return render(request, "player.html", {"player": player_data, "behavior": behavior_data})


def get_match_details(request, match_id):
    match_data = Statistic.objects.select_related('Match').filter(matchid=match_id).values(
        'playerid', 'behavior', 'behaviorcount', 'matchid'
    )
    return render(request, "match.html", {"match_data": match_data})


def get_contrast_details(request, player_id):
    return render(request, "contrast.html")
