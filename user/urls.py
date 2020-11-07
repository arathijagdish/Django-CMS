from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='home'),
    path('<str:url>', viewpost, name='viewpost'),
    path('search/', search, name='searchpost'),
]