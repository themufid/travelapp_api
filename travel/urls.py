
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-agency/', views.create_agency, name='create_agency'),
    path('get-agency/<int:agency_id>/', views.get_agency, name='get_agency'),
    path('create-service/', views.create_service, name='create_service'),
]
