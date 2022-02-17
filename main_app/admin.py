from dataclasses import fields
from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    ordering = ['name'] 

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','city','img','body']

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['title','email','favourite_city','profile_picture']
    


