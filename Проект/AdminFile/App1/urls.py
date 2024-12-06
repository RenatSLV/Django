from django.urls import path
from App1.views import *

urlpatterns = [
    path('', Login_page, name='login_page'),
    path('main/', Main_page, name='main_page'),
]