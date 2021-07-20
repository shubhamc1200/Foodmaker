from django.shortcuts import render
from .models import Lat_Long
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



def getuserIp(request):
    Lat_Long1=Lat_Long.objects.all()
    return render(request,'first_page_map.html',{'Lat_Long1':Lat_Long1})


def update_new_lat_long(request):
    if request.method == 'POST':
        Lat_Long.objects.create( latitude= request.POST['lat'],longitude=request.POST['lng'])
        message = 'create successful'
    return HttpResponse(message)
