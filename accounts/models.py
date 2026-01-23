from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = (
        ('student', 'student'),
        ('admin', 'admin'),
        ('mentor', 'mentor')
    )

    role = models.CharField(max_length=100, choices=ROLES, default='student')
    phone = models.CharField(max_length=15)
    


# class Profile(models.Model):
#     user = models.OneToOneField(CustomUser, 
#         on_delete=models.CASCADE, related_name='profile'
#     )
