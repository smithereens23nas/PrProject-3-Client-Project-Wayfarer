from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home.as_view(), name="home"),
    # Home page when you login as a user.
    # path('accounts/login/', views.Home.as_view(), name="Login"),
    path('countries/', views.CountryList.as_view(), name='country_list'),
    path('countries/new', views.CountryCreate.as_view(), name='country_create'),
    path('countries/<int:pk>/', views.CountryDetail.as_view(), name='country_detail'),
    path('countries/<int:pk>/update', views.CountryUpdate.as_view(), name='country_update'),
    path('countries/<int:pk>/delete', views.CountryDelete.as_view(), name='country_delete'),
    
]