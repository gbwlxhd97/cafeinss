from django.shortcuts import render
from .models import cafeinformation

def index(request):
    return render(request, 'index.html')

def cafe(request):
    cafe = cafeinformation.objects
    return render(request, 'cafe.html', {'cafe': cafe})

