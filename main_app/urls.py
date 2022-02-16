from django.urls import path
from . import views
from .views import PostCreate, ProfileCreate, ProfileEdit, AddPostView

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('signup/', ProfileCreate.as_view(), name="signup"),
    path('profile/edit', ProfileEdit.as_view(), name="profile_edit"),
    path('countries/', views.CountryList.as_view(), name='country_list'),
    path('profile/', views.ProfileDetail.as_view(), name='profile_detail'),
    path('add_post/', PostCreate.as_view(), name='add_post'),
    
    # path('countries/new', views.CountryCreate.as_view(), name='country_create'),
    # path('countries/<int:pk>/', views.CountryDetail.as_view(), name='country_detail'),
    # path('countries/<int:pk>/update', views.CountryUpdate.as_view(), name='country_update'),
    # path('countries/<int:pk>/delete', views.CountryDelete.as_view(), name='country_delete'),
    path('countries/<int:pk>/cities/new', views.CityCreate.as_view(), name='city_create')
]