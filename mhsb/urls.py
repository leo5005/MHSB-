from django.urls import path
from mhsb import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]