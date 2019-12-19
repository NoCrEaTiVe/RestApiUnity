from django.shortcuts import render
from .models import Restaurant,Food
from .serializers import RestaurantSerializer,FoodSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser,JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)
class Foode(APIView):
    parser_class = (JSONParser)
    queryset = (Food.objects.all())
    def post(self, request, *args, **kwargs):

      file_serializer = FoodSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save(name = self.request.data.get('name'))
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 


 
@api_view(['GET'])  
def get_restaurant_information(request,id):
    restaurant = Restaurant.objects.get(id=id)
    serializer = RestaurantSerializer(restaurant,many=False)
    return JSONResponse(serializer.data)
@api_view(['GET'])  
def get_food_information(request,id,foodid):
    food = Food.objects.get(id=foodid)
    serializer = FoodSerializer(food,many=False,context={'request': request})
    return JSONResponse(serializer.data)
