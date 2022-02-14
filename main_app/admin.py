from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'continent']
    
# admin.site.register(models.Country)
@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description','country']