#from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


from .models import Drink
from .serializers import DrinkSerializer
from  rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def drink_list(request):
  if request.method=='GET':

  #get all the drinks
         drinks = Drink.objects.all()
  
  #serialize them
         serializer = DrinkSerializer(drinks, many=True)
  
  #return json
         return JsonResponse(serializer.data, safe=False)
  
  if request.method == 'POST': 
        serializer =  DrinkSerializer(data=request.data) 
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED )
         