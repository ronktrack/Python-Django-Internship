from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('',views.myform,name='myform'),
    path('formprocess',views.process,name='process'),
]