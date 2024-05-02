from django.contrib import admin
from django.urls import path
from world import views
# path('admin/', admin.site.urls)
urlpatterns = [
    path('home/', views.get_standing),
    # path('temp_learn/', views.temp_learn),
    # path('login/', views.login),
    # path('standing/', views.get_standing),
    path('home/<int:team_id>/', views.get_team_details, name='team_detail'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),

]
