from django.db import models
from halls.models import Hall
from images.models import Image
from authentication.models import User
from halls.models import Seat

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    begin = models.TimeField()
    end = models.TimeField()
    images = models.ManyToManyField(Image)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    administrator = models.ForeignKey(User, on_delete=models.CASCADE)


class Application(models.Model):
    status = models.CharField(max_length=10, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat, through='ApplicationSeat')
    

class ApplicationSeat(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)