from django.db import models
from stadiums.models import Stadium

class Hall(models.Model):
    name = models.CharField(max_length=255)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)


class Seat(models.Model):
    number = models.IntegerField()
    row = models.IntegerField()
    sector = models.IntegerField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)