from django.db import models
from halls.models import Hall
from images.models import Image
from authentication.models import User
from halls.models import Seat

class Event(models.Model):
    name = models.CharField(max_length=255)
    images = models.ManyToManyField(Image, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    administrator = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Application(models.Model):
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    status = models.CharField(max_length=10, default='draft')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat, through='ApplicationSeat')
    

class ApplicationSeat(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)