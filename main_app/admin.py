from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'img','body', 'city', 'author']

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','email','profile_picture', 'city']

    
# admin.site.register(models.Country)
@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'description']
    ordering = ['name']