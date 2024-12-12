from django.shortcuts import render
from django.http import HttpResponse
from AppModels.models import *


def get_data(request):
    news_list = News.objects.all()
    return render(request, 'index.html', {'news_list': news_list})
