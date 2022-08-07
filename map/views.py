from django.shortcuts import render
from django.http import JsonResponse 
from map.models import Beach_List
from django.forms.models import model_to_dict


def map(request):
  return render(request, 'map.html')

def map_data(request):
  data = Beach_List.objects.all()
  map_list = []
  for d in data:
    d = model_to_dict(d)  
    map_list.append(d)
  return JsonResponse(map_list, safe=False)