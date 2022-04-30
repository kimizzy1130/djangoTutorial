from django.db import models
from core.models import TimeStampedModel
from users.models import User

# Create your models here.
class Place(TimeStampedModel):
    name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=50, blank=False)
    second_phone_number = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length = 50, blank=False)
    description = models.CharField(max_length=512, blank = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #cascade = user가 없어지면 place도 없어짐 (반대로는 SET_NULL)

    def __str__(self):
        return self.name + "-" + self.owner.username


