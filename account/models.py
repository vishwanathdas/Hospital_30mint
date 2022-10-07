from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', )
    is_patient = models.BooleanField('Is patient', )
    is_doctor = models.BooleanField('Is doctor', )