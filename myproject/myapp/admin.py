# myapp/admin.py

from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'reason', 'academic', 'first_name', 'middle_name', 'last_name', 
        'student_number', 'gender', 'dob', 'college', 'course', 'address', 
        'phone', 'email', 'emergency_name', 'emergency_phone', 'emergency_address', 
        'submitted_at'
    )
    search_fields = (
        'first_name', 'middle_name', 'last_name', 'student_number', 'college', 
        'course', 'address', 'phone', 'email', 'emergency_name', 'emergency_phone', 
        'emergency_address'
    )
    list_filter = (
        'reason', 'academic', 'gender', 'submitted_at'
    )
