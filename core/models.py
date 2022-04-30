from django.db import models

class TimeStampedModel(models, Model):
    created = models.DateTimeField(auto_now_add=True)  #자동 만들어짐
    updated = models.DateTimeField(auto_now=True) #자동 업데이트
    
    class Meta:
        abstract = True
