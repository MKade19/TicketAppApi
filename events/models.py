from django.db import models
from images.models import Image
from authentication.models import User
from stadiums.models import Seat, Hall


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    images = models.ManyToManyField(Image, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    administrator = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Application(models.Model):
    status = models.CharField(max_length=10, default='draft')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat, through='ApplicationSeat')
    

class ApplicationSeat(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)