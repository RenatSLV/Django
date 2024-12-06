from django.shortcuts import render

def Login_page(request):
    return render(request, 'Login.html')

def Main_page(request):
    return render(request, 'Main.html')
