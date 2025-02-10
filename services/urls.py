from django.urls import path 
from .views import services

urlpatterns = [
    path("" , services , name= "services")
]
