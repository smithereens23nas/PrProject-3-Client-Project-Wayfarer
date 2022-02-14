from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.http import HttpResponse
from django.urls import reverse
from .models import Country, City
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

class CountryList(TemplateView):
    template_name = 'country_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['countries'] = Country.objects.filter(name__icontains=name)
            context['header'] = f"Searching For {name}"
        else:
            context['countries'] = Country.objects.all()
            context['header'] = "All The Countries"
        return context


class CountryCreate(CreateView):
    model = Country
    fields = ['name', 'img', 'city', 'continent']
    template_name = 'country_create.html'
    def get_success_url(self):
        return reverse('country_detail', kwargs={'pk': self.object.pk})


class CountryDetail(DetailView):
    model = Country
    template_name = 'country_detail.html'

class CountryUpdate(UpdateView):
    model = Country
    fields = ['name', 'img', 'city', 'continent']
    template_name = 'country_update.html'
    def get_success_url(self):
        return reverse('country_detail', kwargs={'pk': self.object.pk})


class CountryDelete(DeleteView):
    model = Country
    template_name = 'country_delete_confirmation.html'
    success_url = '/countries/'