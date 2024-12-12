from django.contrib import admin
from django.urls import path, include

from AppModels.models import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppModels.urls')),
]
