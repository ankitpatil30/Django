
from django.urls import path
from FIRSTAPPLICATION import views

urlpatterns = [     
    path('home', views.home, name='SixPathsPain Home'),
    path('about', views.about, name='SixPathsPain about'),
    path('contact', views.contact, name='SixPathsPain contacts'),
    path('signup', views.signup, name='SixPathsPain Signup'), 
    path('portfolio', views.portfolio, name='SixPathsPain portfolio'), 
]