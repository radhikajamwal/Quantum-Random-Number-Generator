from django.urls import path
from .views import home,random

urlpatterns = [
    path("", home, name= "home"),
    path("random/",random, name = "random"),
    ]