from django.shortcuts import render
from django.views.generic import View
from .models import Post

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mhsb/index.html')
    
class RenseiView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mhsb/rensei.html')
    
class WeaponView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mhsb/weapon.html')
        