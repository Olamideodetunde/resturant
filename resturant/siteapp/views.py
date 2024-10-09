from django.shortcuts import render
from .models import Reservation,News,Menu,Contact

def index(request):
    menu=Menu.objects.all()
    context={'menu':menu}
    return render(request,'siteapp/index.html',context=context)
def menu(request):
    menu=Menu.objects.all()
    return render(request,'siteapp/menu.html')
def news(request):
    return render(request,'siteapp/news.html')
def about(request):
    return render(request,'siteapp/about.html')
def contact(request):
    return render(request,'siteapp/contact.html')
def single_news(request,slug):
    return render(request,'siteapp/news-detail.html')
