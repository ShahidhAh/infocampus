from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('first/', views.first),
    path('second/', views.second),
]