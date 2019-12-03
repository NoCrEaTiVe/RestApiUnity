from django.contrib import admin
from .models import Category,Food,Restaurant
# Register your models here.
admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Restaurant)