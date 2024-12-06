from django.urls import path
from django.contrib import admin
from App1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
]
