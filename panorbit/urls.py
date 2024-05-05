from django.contrib import admin
from django.urls import path
from world import views
# path('admin/', admin.site.urls)
urlpatterns = [
    path('home/', views.get_standing),
    path('player/<int:player_id>', views.get_player_details, name='player_detail'),
    path('contrast/<int:player_id>', views.get_contrast_details),
    path('match/<int:match_id>/', views.get_team_details, name='match_detail'),
    path('home/<int:team_id>/', views.get_team_details, name='team_detail'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
]
