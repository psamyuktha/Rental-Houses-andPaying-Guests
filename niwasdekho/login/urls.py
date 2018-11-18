from django.urls import path
from login import views

app_name = 'login'


urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.user_profile,name='profile'),
    path('forgot-pass/',views.forget_pass,name='forgot'),
    path('activate/<uidb64>/<token>/',
        views.activate, name='activate'),


]
