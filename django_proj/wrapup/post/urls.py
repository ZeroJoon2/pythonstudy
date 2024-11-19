from django.contrib import admin
from django.urls import path
from .views import *    

urlpatterns = [
    path("", post_list),
    path("<int:id>/", post_detail),
]