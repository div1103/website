from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('about-us/', views.about),
]