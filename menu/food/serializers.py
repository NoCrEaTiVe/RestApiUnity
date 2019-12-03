from rest_framework import serializers
from . models import Restaurant,Food

class RestaurantSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Restaurant
        fields = ('__all__')
class FoodSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    class Meta:
        model = Food 
        fields = ('__all__')    
    def get_photo_url(self, food):
        request = self.context.get('request')
        photo_url = food.image.url
        return request.build_absolute_uri(photo_url)
    
