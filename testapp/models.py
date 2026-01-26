from django.db import models
# from django.utils import timezone


# Create your models here.

# first_name, last_name, photo, desigination, email_address, phone_number, created_at, updated_at

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    desigination = models.CharField(max_length=100)
    email_address= models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)  # Optional --> blank=True
    created_at = models.DateTimeField(auto_now_add=True)  # Store current time when the record is created
    # created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)  # Store current time when the record is updated

    # NEW FIELD
    is_senior = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name