from django.db import models

# Create your models here.
from django.core.validators import MaxValueValidator
from django.db import models

class Thing(models.Model):
    name = models.CharField(unique=True ,max_length=30,blank =False)
    description = models.CharField(unique = False,max_length=120, blank=True)
    quantity = models.PositiveIntegerField(unique=False,validators=[MaxValueValidator(100)])