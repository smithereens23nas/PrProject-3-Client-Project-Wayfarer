from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.http import HttpResponse
from django.urls import reverse
from .models import Country, City
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class Home(TemplateView):
    def get(self, request):
        return render( request, 'home.html')
    
class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html")
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("artist_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
        
class Logout(TemplateView):
    template_name = 'logout_confirmation.html'
    success_url = "/home/"
    

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


class CityCreate(View):
    def post(self, request, pk):
        name = request.POST.get('name')
        img = request.POST.get('img')
        description = request.POST.get('description')
        country = Country.objects.get(pk=pk)
        City.objects.create(name=name, img=img, description=description, country=country)
        return redirect('country_detail', pk=pk)