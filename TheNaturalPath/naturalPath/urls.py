from django.urls import path
from .import views



urlpatterns = [
    path("", views.home, name="np-home"), 
    path("providers/", views.providers, name="providers"),
    path("register/", views.register, name="register"), 
    path("login/", views.login, name="login"), 
    path("logout/", views.logout, name="logout"), 
    path("success/", views.success, name="success"), 
  ]






