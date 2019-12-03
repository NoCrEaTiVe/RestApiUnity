from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from . models import Video
from .serializers import VideoSerializer
from rest_framework.parsers import FileUploadParser,MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



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
 
def index(request):
    return HttpResponse("HelloWorld")
 
@api_view(['GET'])
def videos(request):
    videos = Video.objects.all()
    
    serializer = VideoSerializer(videos, many=True)
    return JSONResponse(serializer.data)
@api_view(['GET'])
def get_videos(request):
    files=Video.objects.all()
    serializer = VideoSerializer(files,many=True)
    return JSONResponse(serializer.data)


@api_view(['POST'])  
def delete_videos(request): 
     Video.objects.all().delete()
     files=Video.objects.all()
     serializer = VideoSerializer(files,many=True)
     return JSONResponse(serializer.data)