from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    GENDER_CHOICES = (("male", "Male"), ("female", "Female")) #왼쪽 = access, 오른쪽 = 사람들에게 보여지는거
    gender = models.CharField(max_length=10, blank=True, choices = GENDER_CHOICES)  #blank = 비어도 되는지
    phone_number = models.CharField(max_length=20)
    is_owner = models.BooleanField(default=False)