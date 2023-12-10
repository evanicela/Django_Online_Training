from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('price', views.price, name='price'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('addproject', views.addproject, name='addproject'),
]
