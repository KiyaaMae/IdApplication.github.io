# myapp/forms.py

from django import forms
from .models import Application
import re
from django.core.exceptions import ValidationError

def validate_student_number(value):
    if not re.match(r'^\d{4}-\d{5}-[A-Z]{2}-\d$', value):
        raise ValidationError('Invalid student number format. It should be YYYY-XXXXX-XX-X.')

def validate_phone(value):
    if not re.match(r'^\+63\d{10}$', value):
        raise ValidationError('Invalid phone number format. It should be +63XXXXXXXXXX.')
    
# New validation function to check if student number already exists
def validate_unique_student_number(value):
    if Application.objects.filter(student_number=value).exists():
        raise ValidationError('Student number already entered. Please try again.')

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'reason', 'academic', 'first_name', 'middle_name', 'last_name', 'student_number', 
            'gender', 'dob', 'college', 'course', 'address', 'phone', 'email', 
            'emergency_name', 'emergency_phone', 'emergency_address'
        ]
        widgets = {
            'reason': forms.RadioSelect,
            'academic': forms.RadioSelect,
            'gender': forms.RadioSelect,
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    student_number = forms.CharField(validators=[validate_student_number, validate_unique_student_number])
    phone = forms.CharField(validators=[validate_phone])
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
            field.required = True
            field.initial = ''  # Ensure the initial value is an empty string
