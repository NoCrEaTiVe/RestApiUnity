from django.db import models

import uuid
import os
def get_upload_path(instance, filename):
    return os.path.join(
        str(instance.restaurant.id),str(instance.id),"image",str(instance.uid))
def get_upload_path2(instance, filename):
    return os.path.join(
      str(instance.id),"models",str(instance.uid))


class Category(models.Model):
    name = models.TextField(max_length=100)
    class Meta:
           verbose_name_plural = "Categories"
class Food(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.TextField(max_length=100)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)
    restaurant = models.ForeignKey("Restaurant",on_delete=models.CASCADE)

    uid  = uuid.uuid4()
    image = models.FileField(upload_to=get_upload_path)

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    uid  = uuid.uuid4()
    #postgis#address =  models.CharField("Longitude,altitude",max_length=200)
    db_file = models.FileField(blank=True, null=False,upload_to=get_upload_path2)
    

