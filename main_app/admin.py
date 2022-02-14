from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'continent']
    
# admin.site.register(models.Country)
