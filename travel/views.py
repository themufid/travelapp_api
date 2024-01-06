
from django.shortcuts import render, redirect
from .models import TravelService, TravelAgency
from .serializers import TravelServiceSerializer, TravelAgencySerializer
from django.http import HttpResponseNotFound

def index(request):
    agencies = TravelAgency.objects.all()
    return render(request, 'index.html', {'agencies': agencies})

def create_agency(request):
    if request.method == 'POST':
        agency_name = request.POST.get('agency_name')
        if agency_name:
            db_agency = TravelAgency(name=agency_name)
            db_agency.save()
    return redirect('index')

def get_agency(request, agency_id):
    try:
        db_agency = TravelAgency.objects.get(id=agency_id)
        return render(request, 'agency_detail.html', {'agency': db_agency})
    except TravelAgency.DoesNotExist:
        return HttpResponseNotFound("Agency not found")

def create_service(request):
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        service_description = request.POST.get('service_description')
        service_price = request.POST.get('service_price')
        service_available_slots = request.POST.get('service_available_slots')
        
        if service_name and service_description and service_price and service_available_slots:
            db_service = TravelService(
                name=service_name,
                description=service_description,
                price=service_price,
                available_slots=service_available_slots,
            )
            db_service.save()
    return redirect('index')
