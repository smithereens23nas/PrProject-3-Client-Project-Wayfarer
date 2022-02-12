from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView
from django.http import HttpResponse
# Create your views here.

class Home(TemplateView):
    def get(self, request):
        return HttpResponse('homepage')
#mock database

class Country:
    def __init__(self, name, image, city, continent):
        self.name = name 
        self.image = image
        self.city = city
        self.continent = continent

#mock database
countries = [
    Country( "United States","https://www.kindpng.com/picc/m/61-611171_us-flag-shape-of-country-hd-png-download.png",["Miami", "Los Angles", "New York"],"North America"),
    Country( "Brazil","https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/brazil-flag-border-gift-country-pride-identity-fan-funny-gift-ideas.jpg",["Rio de Janiero", "Brazilla", "Sao Paulo"],"South America"), 
    Country( "Italy","https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/italy-flag-in-country-silhouette-peter-hermes-furian.jpg",["Rome", "Florence", "Venice"],"Europe"), 
    Country( "Japan","https://ih1.redbubble.net/image.903835950.0919/st,small,845x845-pad,1000x1000,f8f8f8.jpg",["Tokyo","Kyoto","Osaka"],"Asia"), 
    Country( "Australia","https://cdn11.bigcommerce.com/s-plfev599h5/images/stencil/1280x1280/products/55544/168933/41MGRRitBpL__83715.1602574540.jpg?c=1",["Sydney", "Melburne", "Brisbane"],"Australia"),
]


