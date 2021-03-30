
from django.urls import path
from Nagato import views

urlpatterns = [     
    path('', views.home, name='SixPathsPain Home'),
    path('about', views.about, name='SixPathsPain about'),
    path('contact', views.contact, name='SixPathsPain contacts'), 
]