from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainview),
    path('upload/',views.upload_image)    
]