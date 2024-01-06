
from django.db import models

class TravelService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available_slots = models.IntegerField()
    is_available = models.BooleanField(default=True)

class TravelAgency(models.Model):
    name = models.CharField(max_length=100)
    services_offered = models.ManyToManyField(TravelService)
