import pandas as pd
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from world.authentication import EmailBackend
from . import authentication
from .models import Standing, Team, Player, Match, Statistic
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from haystack.query import SearchQuerySet

# excel数据读取
excel_data1 = pd.read_excel('数据话英超.xls')


# Create your views here.
# 第一个位子是视图函数的request参数，第二个参数位是html文件路径
def temp_learn(request):
    user_info = {
        "name": "zm",
        "salary": 100000,
        "role": "CTO",
    }
    name = "zm"
    student = ["first_name", "last_name"]
    return render(request, "templates_learn.html", {"n1": name, "stu_list": student, "user_info": user_info})


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
        return render(request, 'login.html',)
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
                    return redirect('/')
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
    teams = Standing.objects.all()
    return render(request, "home.html", {"teams": teams})


def get_team_details(request, teamid):
    team_data = Team.objects.get(teamid=teamid)
    match_data = Match.objects.filter(teamid=teamid).order_by('date')
    player_data = Player.objects.filter(teamid=teamid).order_by('-prize')
    return render(request, "demo.html", {
        "team_data": team_data,
        "match_data": match_data,
        "player_data": player_data
    })


def get_player_details(request, playerid):
    player_data = Player.objects.get(playerid=playerid)
    return render(request, "player.html", {"player": player_data})


def get_match_details(request, matchid):
    match_data = Statistic.objects.select_related('Match').filter(matchid=matchid).values(
        'playerid', 'behavior', 'behaviorcount', 'matchid'
    )
    return render(request, "match.html", {"match_data": match_data})


def search(request):
    query = request.GET.get("query", "").strip()
    result = {"teams": [], "players": []}

    if not query and len(query) < 3:
        return JsonResponse(result)

    team_pks = list(SearchQuerySet().autocomplete(i_city_name=query).values_list("pk", flat=True))
    player_pks = list(SearchQuerySet().autocomplete(i_country_name=query).values_list("pk", flat=True))

    result["teams"] = [Team.objects.filter(pk=team_pk).values().first() for team_pk in team_pks]
    result["players"] = [Player.objects.filter(pk=player_pk).values().first() for player_pk in player_pks]

    return render(request, "search_results.html", result)


def c_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")