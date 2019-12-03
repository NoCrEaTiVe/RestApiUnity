from django.shortcuts import render
from .models import Restaurant,Food
from .serializers import RestaurantSerializer,FoodSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import FileUploadParser,MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)
@api_view(['GET'])  
def get_restaurant_information(request,id):
    restaurant = Restaurant.objects.get(id=id)
    serializer = RestaurantSerializer(restaurant,many=False)
    return JSONResponse(serializer.data)
@api_view(['GET'])  
def get_food_information(request,id,foodid):
    food = Food.objects.get(id=foodid)
    serializer = FoodSerializer(food,many=True)
    return JSONResponse(serializer.data)
