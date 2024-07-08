from django.db import models
from events.models import Application
from stadiums.models import Seat
from authentication.models import User


class Ticket(models.Model):
    is_sold = models.BooleanField(default=False)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
