from django.urls import path 
from .views import post_detail

app_name = 'services'


urlpatterns = [
    path("<int:id>/" , post_detail , name= "post_detail")
]


