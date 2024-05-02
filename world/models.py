from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 在MySQL中创建对应的一个表
class Team(models.Model):
    '球队建表'
    teamid = models.IntegerField(verbose_name="球队ID", primary_key=True)
    name = models.CharField(verbose_name="球队英文名称", max_length=20, unique=True)
    shortname = models.CharField(verbose_name="球队缩写", max_length=20)
    chinaname = models.CharField(verbose_name="球队中文名称", max_length=20)
    othername = models.CharField(verbose_name="球队中文别名", max_length=20)
    foundtime = models.DateTimeField(verbose_name="成立时间", auto_now=True)
    city = models.CharField(verbose_name="城市", max_length=20)
    home = models.CharField(verbose_name="主场", max_length=20)
    coach = models.CharField(verbose_name="教练", max_length=20)


class Player(models.Model):
    '球员建表'
    playerid = models.IntegerField(verbose_name="球员ID", primary_key=True)
    name = models.CharField(verbose_name="球员名", max_length=20)
    chinaname = models.CharField(verbose_name="球员中文名", max_length=20)
    position = models.CharField(verbose_name="位置", max_length=20)
    nation = models.CharField(verbose_name="国籍", max_length=20)
    age = models.IntegerField(verbose_name="年龄")
    prize = models.CharField(verbose_name="身价", max_length=20)
    num = models.IntegerField(verbose_name="号码")
    teamid = models.ForeignKey(
        verbose_name="球队ID",
        to="Team",
        to_field="teamid",
        db_column='teamid',
        on_delete=models.CASCADE
    )


class Match(models.Model):
    '赛程建表'
    matchid = models.IntegerField(verbose_name="赛程ID", primary_key=True)
    hostteamid = models.ForeignKey(
        verbose_name="主队ID",
        to="Team",
        to_field="teamid",
        db_column='hostteamid',
        related_name="host_match",
        on_delete=models.CASCADE
    )
    guestteamid = models.ForeignKey(
        verbose_name="客队ID",
        to="Team",
        to_field="teamid",
        db_column='guestteamid',
        related_name="guest_match",
        on_delete=models.CASCADE
    )
    hostgoal = models.IntegerField(verbose_name="主队分数")
    guestgoal = models.IntegerField(verbose_name="客队分数")
    date = models.DateTimeField(verbose_name="比赛日期", auto_now=True)
    status_choices = (
        (1, "已结束"),
        (2, "进行中"),
        (3, "未比赛"),
    )
    status = models.SmallIntegerField(verbose_name="比赛状态", choices=status_choices)


class Statistic(models.Model):
    '比赛数据建表'
    playerid = models.ForeignKey(
        verbose_name="球员ID",
        to="Player",
        to_field="playerid",
        db_column='playerid',
        on_delete=models.CASCADE
    )
    behavior_choices = (
        (1, "GOAL"),
        (2, "PENALTY"),
        (3, "ASSIST"),
        (4, "CLEARANCE"),
        (5, "TACKLE"),
        (6, "REDCARD"),
        (7, "YELLOWCARD"),
        (8, "OFFSIDE"),
    )
    behavior = models.SmallIntegerField(verbose_name="球员行为", choices=behavior_choices)
    behaviorcount = models.IntegerField(verbose_name="行为数量", default=0)
    matchid = models.ForeignKey(
        verbose_name="赛程ID",
        to="Match",
        to_field="matchid",
        db_column='matchid',
        on_delete=models.CASCADE
    )


class Standing(models.Model):
    '球队积分建表'
    teamid = models.IntegerField(
        verbose_name="排名",
        primary_key=True
    )
    name = models.CharField(verbose_name="球队名", max_length=40)
    sum = models.IntegerField(verbose_name="场次",
                              default=0)
    goals = models.IntegerField(verbose_name="进球数", default=0)
    miss = models.IntegerField(verbose_name="失球数",
                               default=0)
    clear = models.IntegerField(verbose_name="净胜球", default=0)
    points = models.IntegerField(verbose_name="积分", default=0)




