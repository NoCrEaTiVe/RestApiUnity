from django.db import models
from food.models import Food
import os
import uuid
def get_upload_path(instance, filename):
    return os.path.join(
        str(instance.food.restaurant.id),str(instance.food.id),"video",str(instance.uid))

class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food = models.OneToOneField("food.Food",on_delete=models.CASCADE)
    uid  = uuid.uuid4()
    file = models.FileField(blank=True, null=False,upload_to=get_upload_path)
    title = models.CharField(max_length = 60)
    description = models.TextField()
    class Meta:
           verbose_name_plural = "Videos"
 
    def __str__(self):
        return self.title
 
