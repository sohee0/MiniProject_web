# from django.http import HttpResponse
# from django.shortcuts import render

from http.client import HTTP_PORT
import imp
from unittest import loader
import wave

from django.http import HttpResponse
from django.shortcuts import render
import BeachData
from BeachData.models import  Wave
from .models import Wave

# Create your views here.
def index(request):
    return render(request, 'BeachData/index.html')


def test(request):
    beach_name = request.GET.get('beach_name')
    # wave = Wave.objects.all()
    wave = Wave.objects.filter(beach_name__contains=beach_name)
    return render(request,'BeachData/list.html',
    {'wave_list':wave[:10], 'img': beach_name})


def static(request):
    return render(request, 'BeachData/static.html')
    


    
