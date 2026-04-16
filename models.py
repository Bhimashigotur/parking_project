from django.db import models

class Category(models.Model):
    parking_area_no = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100)
    vehicle_limit = models.IntegerField()
    parking_charge = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)


class Vehicle(models.Model):
    vehicle_no = models.CharField(max_length=100)
    parking_area_no = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100)
    parking_charge = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Parked')
    arrival_time = models.DateTimeField(auto_now_add=True)
