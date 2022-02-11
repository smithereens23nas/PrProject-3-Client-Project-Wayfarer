from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView
from django.http import HttpResponse
# Create your views here.

class Home(TemplateView):
    def get(self, request):
        return HttpResponse('homepage')


