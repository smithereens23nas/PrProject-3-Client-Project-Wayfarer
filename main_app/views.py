from dataclasses import fields
from re import template
from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse, reverse_lazy
from .models import Country, City, Profile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import SignUpForm
# Create your views here.

class Home(TemplateView):
    def get(self, request):
        return render( request, 'home.html')
    
# class Signup(View):
#     def get(self, request):
#         form = UserCreationForm()
#         context = {"form": form}
#         return render(request, "registration/signup.html")
    
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("country_list")
#         else:
#             context = {"form": form}
#             return render(request, "registration/signup.html", context)
        
class ProfileCreate(CreateView):
    form_class = SignUpForm
    model = Profile
    fields = ['user_name', 'email', 'current_city', 'profile_picture']
    template_name = 'registration/profile_create.html'
    success_url = reverse_lazy('login')

class ProfileEdit(UpdateView):
    form_class = UserChangeForm
    model = Profile
    fields = ['user_name', 'email', 'current_city', 'profile_picture']
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user


class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    
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


# class CountryCreate(CreateView):
#     model = Country
#     fields = ['name', 'img', 'city', 'continent']
#     template_name = 'country_create.html'
#     def get_success_url(self):
#         return reverse('country_detail', kwargs={'pk': self.object.pk})


# class CountryDetail(DetailView):
#     model = Country
#     template_name = 'country_detail.html'

# class CountryUpdate(UpdateView):
#     model = Country
#     fields = ['name', 'img', 'city', 'continent']
#     template_name = 'country_update.html'
#     def get_success_url(self):
#         return reverse('country_detail', kwargs={'pk': self.object.pk})


# class CountryDelete(DeleteView):
#     model = Country
#     template_name = 'country_delete_confirmation.html'
#     success_url = '/countries/'


class CityCreate(View):
    def post(self, request, pk):
        name = request.POST.get('name')
        img = request.POST.get('img')
        description = request.POST.get('description')
        country = Country.objects.get(pk=pk)
        City.objects.create(name=name, img=img, description=description, country=country)
        return redirect('country_detail', pk=pk)