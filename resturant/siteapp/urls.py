from . import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='home-page'),
    path('about/',views.about,name='about-page'),
    path('news/',views.news,name='news-page'),
    path('menu/',views.menu,name='menu-page'),
    path('news-detail/<slug:slug>',views.single_news,name='news-detail'),
    path('contact/',views.contact,name='contact-page'),
]
