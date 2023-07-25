from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def mainpage(request):
    return render(request, 'pages/mainpage.html')
def company(request):
    return render(request, 'pages/company_info.html')
def mainmain(request):
    return render(request, 'pages/main_mainpage.html')
def login(request):
    return render(request, 'pages/logIn_page.html')
def login_new(request):
    return render(request, 'pages/logIn_new.html')
def login_search(request):
    return render(request, 'pages/logIn_search.html')
def item1(request):
    return render(request, 'pages/item1.html')
def item2(request):
    return render(request, 'pages/item2.html')
