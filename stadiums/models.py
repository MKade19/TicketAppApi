from django.db import models
from cities.models import City
from images.models import Image
from users.models import User

class Stadium(models.Model):
    name = models.CharField(max_length=255)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    administrator = models.ForeignKey(User, on_delete=models.CASCADE)