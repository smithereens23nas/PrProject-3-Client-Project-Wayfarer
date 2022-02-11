from django.urls import path
from . import views

urlpatterns = [
    path('/home/', views.Home.as_view(), name="home"),
    # Home page when you login as a user.
    # path('accounts/login/', views.Home.as_view(), name="Login"),
    
]