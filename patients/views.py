from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from appointments.forms import BookingAppointmentForm
from appointments.models import Appointment
from patients.forms import RegistrationForm, CustomRegistration
from user_profile.models import UserProfile
from user_profile.utils import unique_id_generator

User = get_user_model()


# Create your views here.

def home(request):
    return render(request, 'patients/home.html')


def patient_create(request):
    registration_form = RegistrationForm(request.POST or None)

    custom_form = CustomRegistration(request.POST or None)

    if registration_form.is_valid() and custom_form.is_valid():
        registration = registration_form.save()
        registration.is_patient = True
        registration.save()
        custom = custom_form.save(commit=False)
        custom.user = registration
        custom.save()

        messages.success(request, 'Patient registered successfully.')
        return redirect('users:patient_list')
    template_name = 'patients/patient_create.html'
    context = {'patient_form': registration_form, 'user_form': custom_form}
    return render(request, template_name, context)


def patient_edit(request, pk):
    patient = get_object_or_404(User, id=pk)
    form = RegistrationForm(request.POST or None, instance=patient)
    if form.is_valid():
        patient = form.save()
        patient.is_patient = True
        patient.save()
        messages.success(request, 'Patient has been edited successfully.')
        return redirect('patients:patient_edit', pk)
    template_name = 'patients/patient_edit.html'
    context = {'form': form, 'patients_list': patient}
    return render(request, template_name, context)


def patient_disable(request, pk):
    patients = get_object_or_404(User, id=pk)
    patients.is_active = False
    patients.save()
    messages.success(request, 'Patient has been disabled.')
    return redirect('users:patient_list')


