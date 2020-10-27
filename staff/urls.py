from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='staff_home'),
    path('post/new', new_post, name='staff_post_creation'),
    path('post/delete/<int:id>', delete_post, name='staff_post_delete'),
]