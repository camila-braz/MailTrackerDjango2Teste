from django.urls import path
from .views import image_load

urlpatterns = [
   # path("", homePageView, name="home"),
    path("" , image_load, name='image_load'),
]

