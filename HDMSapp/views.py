# type: ignore

from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient

def index(request):
    return render(request, 'index.html')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients_list.html', {'patients': patients})

def add_patient(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        disease = request.POST['disease']
        Patient.objects.create(name=name, age=age, disease=disease)
        return redirect('patient_list')
    return render(request, 'add_patient.html')

def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('patient_list')

