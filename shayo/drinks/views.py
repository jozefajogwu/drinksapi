from django.shortcuts import render
from django.http import HttpResponse
from .models import Drink
from .serializers import DrinkSerializer

# Create your views here.
def drink_list(request):

  #get all the drinks
  drinks = Drink.objects(all)
  serializer = DrinkSerializer(drinks, many=True)
  return JsonResponse(serializer.data, safe=False)
  
