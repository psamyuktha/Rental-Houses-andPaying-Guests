from django.contrib import admin
from django.urls import path
from appbasic import views

app_name = 'appbasic'


urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.user_profile,name='profile'),
    path('upload/',views.Pro_upload,name="upload"),
    path('signup/', views.signup, name='signup'),

    path('activate/<uidb64>/<token>/',
        views.activate, name='activate'),


]
