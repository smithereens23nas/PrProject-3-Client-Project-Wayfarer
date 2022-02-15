from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Post)
class Post(admin.ModelAdmin):
    list_display = [ 'city', 'title', 'img','description']
    city =models.CharField(max_length=30)
    title =models.CharField(max_length=100)
    description = models.TextField(max_length=300)
@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'continent']
    ordering = ['name']
    
# admin.site.register(models.Country)
@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'description','country']
    ordering = ['name']