# myapp/views.py

from django.shortcuts import render, redirect
from django.db import IntegrityError  # Import IntegrityError
from .forms import ApplicationForm
from .models import Application

def home(request):
    return render(request, 'home.html')

def apply(request):
    error_message = None

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')  # Redirect to home or another page after successful submission
            except IntegrityError:
                error_message = 'Student number already recorded. Please input another student number.'
    else:
        form = ApplicationForm()

    return render(request, 'apply.html', {'form': form, 'error_message': error_message})

def about(request):
    return render(request, 'about.html')


def team(request):
    return render(request, 'team.html')
