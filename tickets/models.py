from django.db import models
from events.models import ApplicationSeat
from authentication.models import User

class Ticket(models.Model):
    is_sold = models.BooleanField()
    application_seat = models.ForeignKey(ApplicationSeat, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
