# type: ignore

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('add/', views.add_patient, name='add_patient'),
    path('delete/<int:pk>/', views.delete_patient, name='delete_patient'),
]
