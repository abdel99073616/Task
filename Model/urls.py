from django.urls import path
from .views import *
urlpatterns = [
    path('' , loginpage , name='login' ),
    path('register/' , register , name='register'),
    path('home/' , home , name='home'),



]
