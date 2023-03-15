from django.urls import path
from mhsb import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('mhsb/rensei/', views.RenseiView.as_view(), name='rensei'),
]
