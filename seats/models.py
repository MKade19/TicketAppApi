from django.db import models
from halls.models import Hall

class Seat(models.Model):
    number = models.IntegerField()
    row = models.IntegerField()
    sector = models.IntegerField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)