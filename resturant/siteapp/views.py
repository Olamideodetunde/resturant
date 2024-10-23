from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Reservation,News,Menu,Contact
from .forms import ContactForm,ReservationForm
def index(request):
    menu=Menu.objects.all()
    context={'menu':menu}
    return render(request,'siteapp/index.html',context=context)
def reservation(request):
        if request.method=='POST':
            form=ReservationForm(request.POST)
            if form.is_valid():
                form.save()
            return render(request,'siteapp/reservations.html',{'form':form})
        else:
            form=ReservationForm()
            return render(request,'siteapp/reservations.html',{'form':form})
def menu(request):
    menu=Menu.objects.all()
    return render(request,'siteapp/menu.html')
def news(request):
    return render(request,'siteapp/news.html')
def about(request):
    return render(request,'siteapp/about.html')
def contact(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'siteapp/contact.html',{'form':form})
    else:
       form=ContactForm() 
    return render(request,'siteapp/contact.html',{'form':form})
def single_news(request,slug):
    return render(request,'siteapp/news-detail.html')
