from django.conf.urls import url
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView


app_name = 'project'

urlpatterns = [
        url(r'^$', views.home, name="home"),
        url(r'^login/$',views.login_view, name="login"),
        url(r'^logout/$',views.logout_view, name="logout"),
        url(r'^booking/$', views.booking, name='booking'),
        url(r'^bookRoom/$', views.bookRoom, name='bookRoom'),
        url(r'^bookHostel/$', views.bookHostel, name='bookHostel'),
        url(r'^booking_house/$', views.booking_house, name='booking_house'),
        url(r'^booking_hostel/$', views.booking_hostel, name='booking_hostel'),
        url(r'^cancel_booking/$', views.cancelbooking, name='cancelbooking'),
        url(r'^viewbookings/$', views.mybookings, name='viewbookings'),

]

urlpatterns += staticfiles_urlpatterns()