from . import views
from django.urls import path

app_name="foodmakerapp"
urlpatterns=[
path('', views.getuserIp, name='getuserIpname'),
path('update_new_lat_long/', views.update_new_lat_long,name='update_new_lat_long')
]
