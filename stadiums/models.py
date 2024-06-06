from django.db import models
from images.models import Image
from authentication.models import User

class City(models.Model):
    name = models.CharField(max_length=255)

class Stadium(models.Model):
    name = models.CharField(max_length=255)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    administrator = models.ForeignKey(User, on_delete=models.CASCADE)


class Hall(models.Model):
    name = models.CharField(max_length=255)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)


class Seat(models.Model):
    number = models.IntegerField()
    row = models.IntegerField()
    sector = models.IntegerField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
