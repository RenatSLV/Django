from django.contrib import admin
from django.urls import path
from AppModels.views import *

urlpatterns = [
    path('index/', index, name='index'),
]