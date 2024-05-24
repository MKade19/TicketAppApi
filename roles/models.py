from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=30)
    permission_hall = models.CharField(max_length=50, blank=True, null=True)
    permission_seat = models.CharField(max_length=50, blank=True, null=True)
    permission_application = models.CharField(max_length=50, blank=True, null=True)
    permission_event = models.CharField(max_length=50, blank=True, null=True)
    permission_stadium = models.CharField(max_length=50, blank=True, null=True)
    permission_ticket = models.CharField(max_length=50, blank=True, null=True)
    permission_user = models.CharField(max_length=50, blank=True, null=True)
