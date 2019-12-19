from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from . models import Video
from food.models import Food
from food.serializers import FoodSerializer
from .serializers import VideoSerializer
from rest_framework.parsers import FileUploadParser,MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from collections import Counter


class FileUploadView(APIView):
    parser_class = (MultiPartParser,FileUploadParser)
    queryset = (Video.objects.all())
    def post(self, request, *args, **kwargs):

      file_serializer = VideoSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save(file = self.request.data.get('file'))
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)
 




@api_view(['GET'])  
def get_food_information(request,id,foodid):
    food = Food.objects.get(id=foodid)
    video = Video.objects.get(food=food)
    serializer2 = VideoSerializer(video,many=False,
    )
    serializer = FoodSerializer(food,many=False,context={'request': request})
    b=serializer.data
    b["videofile"] = serializer2.data["file"]
    
    return JSONResponse(b) 