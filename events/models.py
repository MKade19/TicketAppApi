from django.db import models
from halls.models import Hall
from images.models import Image
from users.models import User

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    begin = models.TimeField()
    end = models.TimeField()
    images = models.ManyToManyField(Image)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    administrator = models.ForeignKey(User, on_delete=models.CASCADE)
