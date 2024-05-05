# Generated by Django 5.0.4 on 2024-05-05 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_alter_statistic_player_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostteam', models.CharField(max_length=10)),
                ('guestteam', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=20)),
                ('hostwin', models.CharField(default=0, max_length=20)),
                ('draw', models.CharField(default=0, max_length=20)),
                ('guestwin', models.CharField(default=0, max_length=20)),
                ('hostgoal', models.IntegerField(default=0)),
                ('guestgoal', models.IntegerField(default=0)),
                ('hostcontrol', models.IntegerField(default=0)),
                ('guestcontrol', models.IntegerField(default=0)),
                ('hostatk', models.IntegerField(default=0)),
                ('guestats', models.IntegerField(default=0)),
                ('hostdanstk', models.IntegerField(default=0)),
                ('guestdanstk', models.IntegerField(default=0)),
                ('hostdirect', models.IntegerField(default=0)),
                ('guestdirect', models.IntegerField(default=0)),
                ('hostaway', models.IntegerField(default=0)),
                ('guestaway', models.IntegerField(default=0)),
                ('hostcornor', models.IntegerField(default=0)),
                ('guestcornor', models.IntegerField(default=0)),
                ('hostpoint', models.IntegerField(default=0)),
                ('guestpoint', models.IntegerField(default=0)),
                ('hostyelloe', models.IntegerField(default=0)),
                ('guestyellow', models.IntegerField(default=0)),
                ('hostred', models.IntegerField(default=0)),
                ('guestred', models.IntegerField(default=0)),
                ('matchid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.match')),
            ],
        ),
    ]
