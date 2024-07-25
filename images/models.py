from django.db import models
from datetime import datetime

def upload_to(instance, filename):
    current_time = datetime.today()
    return 'images/{current_time}-{filename}'.format(filename=filename, current_time=current_time)

class Image(models.Model):
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
