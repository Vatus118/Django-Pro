from django.contrib import admin
from django.urls import path, re_path
from world import views
# path('admin/', admin.site.urls)
urlpatterns = [
    # path('home/', views.get_standing),
    # path('temp_learn/', views.temp_learn),
    # path('login/', views.login),
    # path('standing/', views.get_standing),
    path('home/<int:team_id>/', views.get_team_details, name='team_detail'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),

    # 使用re_path来处理正则表达式
    re_path(r'^search/$', views.search, name="search"),
    path('team/<int:team_id>/', views.get_team_details, name='team_detail'),

    # home路径即是根路径
    re_path(r'^$', views.get_standing, name='home'),
    re_path(r'^logout$', views.c_logout, name="logout"),
]
