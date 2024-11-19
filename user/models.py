from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('COMPANY', 'Компания'),
        ('APPLICANT', 'Соискатель'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
