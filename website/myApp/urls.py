from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'myApp'


urlpatterns = [
    # /myApp/
    path('', views.index, name='index'),

    # /myApp/album_id/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /myApp/album_id/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
