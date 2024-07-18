# myapp/models.py

from django.db import models

class Application(models.Model):
    REASON_CHOICES = [
        ('Transferee', 'Transferee'),
        ('Shiftee', 'Shiftee'),
        ('Late Filing', 'Late Filing'),
        ('Damaged', 'Damaged'),
        ('Old ID', 'Old ID'),
        ('Correction of Entry', 'Correction of Entry'),
    ]

    ACADEMIC_CHOICES = [
        ('LHS', 'LHS'),
        ('SHS', 'SHS'),
        ('Undergrad', 'Undergrad'),
        ('Graduate School', 'Graduate School'),
        ('Open University', 'Open University'),
        ('College of Law', 'College of Law'),
        ('Institute of Technology', 'Institute of Technology'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    reason = models.CharField(max_length=50, choices=REASON_CHOICES)
    academic = models.CharField(max_length=50, choices=ACADEMIC_CHOICES)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_number = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    dob = models.DateField()
    college = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    emergency_name = models.CharField(max_length=100)
    emergency_phone = models.CharField(max_length=20)
    emergency_address = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.student_number}'
