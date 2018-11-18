from django.urls import path
from . import views

urlpatterns = [
    path('basic/', views.plz,name='basic-home'),
    path('basic/iframe', views.plz1,name='basic-iframe'),
    path('basic/block', views.plz2,name='basic-block'),
    #path('basic/variable', views.plz3,name='basic-variables'),
    path('basic/maps', views.plz4,name='basic-maps'),
    #path('basic/new', views.plz5,name='basic-new'),

]
