from django.db import models
from stadiums.models import Stadium

class Hall(models.Model):
    name = models.CharField(max_length=255)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
