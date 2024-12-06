from django.contrib import admin
from django.urls import path, include
from App1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login_page, name='login_page'),
    path('main/', Main_page, name='main_page'),
]
