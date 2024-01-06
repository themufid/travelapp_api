
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.templating import Jinja2Templates
from django.db import models
from fastapi.responses import HTMLResponse
from fastapi import Form
from travel.models import TravelService, TravelAgency
from travel.serializers import TravelServiceSerializer, TravelAgencySerializer

app = FastAPI()
templates = Jinja2Templates(directory="travel/templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    agencies = TravelAgency.objects.all()
    return templates.TemplateResponse("index.html", {"request": request, "agencies": agencies})

@app.post("/create-service/", response_model=TravelServiceSerializer, response_class=HTMLResponse)
async def create_service(
    service_name: str = Form(...),
    service_description: str = Form(...),
    service_price: float = Form(...),
    service_available_slots: int = Form(...),
):
    db_service = TravelService(
        name=service_name,
        description=service_description,
        price=service_price,
        available_slots=service_available_slots,
    )
    db_service.save()
    return db_service

@app.post("/create-agency/", response_model=TravelAgencySerializer, response_class=HTMLResponse)
async def create_agency(agency_name: str = Form(...)):
    db_agency = TravelAgency(name=agency_name)
    db_agency.save()
    return db_agency

@app.get("/get-agency/{agency_id}", response_model=TravelAgencySerializer)
async def get_agency(agency_id: int, request: Request):
    try:
        db_agency = TravelAgency.objects.get(id=agency_id)
        return templates.TemplateResponse("agency_detail.html", {"request": request, "agency": db_agency})
    except TravelAgency.DoesNotExist:
        raise HTTPException(status_code=404, detail="Agency not found")
