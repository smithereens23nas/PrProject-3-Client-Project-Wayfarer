from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('logout/', views.Logout.as_view(), name="logout_confirmation"),
    path('countries/', views.CountryList.as_view(), name='country_list'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('countries/new', views.CountryCreate.as_view(), name='country_create'),
    path('countries/<int:pk>/', views.CountryDetail.as_view(), name='country_detail'),
    path('countries/<int:pk>/update', views.CountryUpdate.as_view(), name='country_update'),
    path('countries/<int:pk>/delete', views.CountryDelete.as_view(), name='country_delete'),
    path('countries/<int:pk>/cities/new', views.CityCreate.as_view(), name='city_create')
]