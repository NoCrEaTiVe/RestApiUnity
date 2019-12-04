from rest_framework import serializers
from . models import Video
from food.serializers import FoodSerializer

    
class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('__all__')

