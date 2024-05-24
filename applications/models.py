from django.db import models
from events.models import Event
from seats.models import Seat

class Application(models.Model):
    status = models.CharField(max_length=10, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat, through='ApplicationSeat')
    

class ApplicationSeat(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
