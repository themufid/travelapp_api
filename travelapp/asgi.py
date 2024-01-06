
import os
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travelapp.settings')

application = get_asgi_application()
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])
