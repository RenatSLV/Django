from django.contrib import admin
from django.urls import path
from AppModels.views import *

urlpatterns = [
    path('get_data/', get_data, name='get_data'),

]