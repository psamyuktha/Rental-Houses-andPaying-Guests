from django.urls import re_path, include, path
from . import views
urlpatterns = [
    path('sam/', views.home , name='home'),


]