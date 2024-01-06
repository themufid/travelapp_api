
from pydantic import BaseModel
from typing import List

class TravelServiceSerializer(BaseModel):
    name: str
    description: str
    price: float
    available_slots: int
    is_available: bool

class TravelAgencySerializer(BaseModel):
    name: str
    services_offered: List[TravelServiceSerializer]
