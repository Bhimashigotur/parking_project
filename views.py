from django.shortcuts import render
from .models import Category, Vehicle

def dashboard(request):
    total_vehicles = Vehicle.objects.count()
    parked = Vehicle.objects.filter(status='Parked').count()

    return render(request, 'dashboard.html', {
        'total_vehicles': total_vehicles,
        'parked': parked
    })
