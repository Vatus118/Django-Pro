from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# 在MySQL中创建对应的一个表
class Team(models.Model):
    '球队建表'
    teamid = models.IntegerField(verbose_name="球队ID", primary_key=True)
    name = models.CharField(verbose_name="球队英文名称", max_length=40, unique=True)
    shortname = models.CharField(verbose_name="球队缩写", max_length=20, unique=True)

    def __str__(self):
        return self.shortname

    chinaname = models.CharField(verbose_name="球队中文名称", max_length=20)
    othername = models.CharField(verbose_name="球队中文别名", max_length=50)
    foundtime = models.CharField(verbose_name="成立时间", max_length=20)
    city = models.CharField(verbose_name="城市", max_length=20)
    home = models.CharField(verbose_name="主场", max_length=30)
    coach = models.CharField(verbose_name="教练", max_length=30)


class Player(models.Model):
    '球员建表'
    playerid = models.IntegerField(verbose_name="球员ID", primary_key=True)
    icon_filename = models.CharField(verbose_name="头像", max_length=160, default='default_icon.png')
    name = models.CharField(verbose_name="球员名", max_length=50)
    chinaname = models.CharField(verbose_name="球员中文名", max_length=40, default="none")
    position = models.CharField(verbose_name="位置", max_length=20, default="none")
    nation = models.CharField(verbose_name="国籍", max_length=40, default="none")
    height = models.IntegerField(verbose_name="身高", default=0)
    weight = models.IntegerField(verbose_name="体重", default=0)
    age = models.IntegerField(verbose_name="年龄", default=0)
    prize = models.CharField(verbose_name="身价", max_length=20, default="none")
    teamname = models.ForeignKey(
        verbose_name="球队",
        to="Team",
        to_field="name",
        db_column='teamname',
        on_delete=models.CASCADE,
        default="None"
    )


class Match(models.Model):
    '赛程建表'
    matchid = models.IntegerField(verbose_name="赛程ID", primary_key=True)
    hostteamid = models.ForeignKey(
        verbose_name="主队",
        to="Team",
        to_field="shortname",
        db_column='hostteamid',
        related_name="host_match",
        on_delete=models.CASCADE,
    )
    guestteamid = models.ForeignKey(
        verbose_name="客队",
        to="Team",
        to_field="shortname",
        db_column='guestteamid',
        related_name="guest_match",
        on_delete=models.CASCADE,
    )
    hostgoal = models.IntegerField(verbose_name="主队分数")
    guestgoal = models.IntegerField(verbose_name="客队分数")
    date = models.CharField(verbose_name="比赛日期", max_length=20)
    status = models.CharField(verbose_name="比赛状态", max_length=10)


class Statistic(models.Model):
    '球员数据建表'
    player_id = models.IntegerField(
        verbose_name="球员ID",
        primary_key=True
    )
    name = models.CharField(verbose_name="球员名", max_length=40, default="None")
    matchsum = models.IntegerField(verbose_name="比赛场次", default=0)
    sum = models.IntegerField(verbose_name="上场场次", default=0)
    first = models.IntegerField(verbose_name="首发", default=0)
    matchtime = models.IntegerField(verbose_name="出场时间", default=0)
    goal = models.IntegerField(verbose_name="进球", default=0)
    penalty = models.IntegerField(verbose_name="点球", default=0)
    shooting = models.IntegerField(verbose_name="射门", default=0)
    target = models.IntegerField(verbose_name="射正", default=0)
    passing = models.IntegerField(verbose_name="过人", default=0)
    valid_passing = models.IntegerField(verbose_name="过人成功", default=0)
    free = models.IntegerField(verbose_name="任意球", default=0)
    free_goal = models.IntegerField(verbose_name="任意球得分", default=0)
    hitdoor = models.IntegerField(verbose_name="击中门框", default=0)
    quick = models.IntegerField(verbose_name="快攻", default=0)
    quick_atk = models.IntegerField(verbose_name="快攻进攻", default=0)
    quick_goal = models.IntegerField(verbose_name="快攻进球", default=0)
    lost_right = models.IntegerField(verbose_name="丢失球权", default=0)
    passball = models.IntegerField(verbose_name="传球", default=0)
    valid_passball = models.IntegerField(verbose_name="传球成功", default=0)
    key_passball = models.IntegerField(verbose_name="关键传球", default=0)
    midpass = models.IntegerField(verbose_name="传中球", default=0)
    valid_midpass = models.IntegerField(verbose_name="传中球成功", default=0)
    longpass = models.IntegerField(verbose_name="长传", default=0)
    valid_longpass = models.IntegerField(verbose_name="长传成功", default=0)
    lost_pass = models.IntegerField(verbose_name="传球被断", default=0)
    breaking = models.IntegerField(verbose_name="解围", default=0)
    valid_prevent = models.IntegerField(verbose_name="有效阻挡", default=0)
    intercept = models.IntegerField(verbose_name="拦截", default=0)
    preemption = models.IntegerField(verbose_name="抢断", default=0)
    onebyone = models.IntegerField(verbose_name="1对1拼抢", default=0)
    valid_onebyone = models.IntegerField(verbose_name="1对1拼抢成功", default=0)
    handball = models.IntegerField(verbose_name="拳击球", default=0)
    keeper_atk = models.IntegerField(verbose_name="守门员出击", default=0)
    valid_atk = models.IntegerField(verbose_name="守门员出击成功", default=0)
    high_atk = models.IntegerField(verbose_name="高空出击", default=0)
    redcard = models.IntegerField(verbose_name="红牌", default=0)
    yellowcard = models.IntegerField(verbose_name="黄牌", default=0)
    foul = models.IntegerField(verbose_name="犯规", default=0)
    violated = models.IntegerField(verbose_name="被侵犯", default=0)
    offside = models.IntegerField(verbose_name="越位", default=0)
    turnred = models.IntegerField(verbose_name="两黄变红", default=0)


class Standing(models.Model):
    '球队积分建表'
    teamid = models.IntegerField(
        verbose_name="排名",
        primary_key=True
    )
    icon_filename = models.CharField(verbose_name="图标", max_length=150, default='default_icon.png')
    name = models.CharField(verbose_name="球队名", max_length=40)
    sum = models.IntegerField(verbose_name="场次",
                              default=0)
    goals = models.IntegerField(verbose_name="进球数", default=0)
    miss = models.IntegerField(verbose_name="失球数",
                               default=0)
    clear = models.IntegerField(verbose_name="净胜球", default=0)
    points = models.IntegerField(verbose_name="积分", default=0)


class Details(models.Model):
    matchid = models.OneToOneField(to="Match", to_field="matchid", db_column='matchid', on_delete=models.CASCADE,
                                   primary_key=True)
    hostteam = models.CharField(max_length=10)
    guestteam = models.CharField(max_length=10)
    date = models.CharField(max_length=20)
    hostwin = models.CharField(max_length=20, default=0)
    draw = models.CharField(max_length=20, default=0)
    guestwin = models.CharField(max_length=20, default=0)
    hostgoal = models.IntegerField(default=0)
    guestgoal = models.IntegerField(default=0)
    hostcontrol = models.IntegerField(default=0)
    guestcontrol = models.IntegerField(default=0)
    hostatk = models.IntegerField(default=0)
    guestatk = models.IntegerField(default=0)
    hostdanatk = models.IntegerField(default=0)
    guestdanatk = models.IntegerField(default=0)
    hostdirect = models.IntegerField(default=0)
    guestdirect = models.IntegerField(default=0)
    hostaway = models.IntegerField(default=0)
    guestaway = models.IntegerField(default=0)
    hostcornor = models.IntegerField(default=0)
    guestcornor = models.IntegerField(default=0)
    hostpoint = models.IntegerField(default=0)
    guestpoint = models.IntegerField(default=0)
    hostyellow = models.IntegerField(default=0)
    guestyellow = models.IntegerField(default=0)
    hostred = models.IntegerField(default=0)
    guestred = models.IntegerField(default=0)


class Score(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    shoot = models.IntegerField(default=0)
    passball = models.IntegerField(default=0)
    physics = models.IntegerField(default=0)
    dribble = models.IntegerField(default=0)
    defensive = models.IntegerField(default=0)
    discipline = models.IntegerField(default=0)
