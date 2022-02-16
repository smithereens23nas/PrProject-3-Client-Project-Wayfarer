from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Post)

class PostAdmin(admin.ModelAdmin):
    list_display = [ 'current_city', 'title', 'img','description']

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','current_city','profile_picture']


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'continent']
    ordering = ['name']
    
# admin.site.register(models.Country)
@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'description','country']
    ordering = ['name']