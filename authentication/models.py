from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=30)
    permission_hall = models.CharField(max_length=50, blank=True, null=True)
    permission_seat = models.CharField(max_length=50, blank=True, null=True)
    permission_application = models.CharField(max_length=50, blank=True, null=True)
    permission_application_status = models.CharField(max_length=50, blank=True, null=True)
    permission_event = models.CharField(max_length=50, blank=True, null=True)
    permission_stadium = models.CharField(max_length=50, blank=True, null=True)
    permission_ticket = models.CharField(max_length=50, blank=True, null=True)
    permission_user = models.CharField(max_length=50, blank=True, null=True)


class User(AbstractUser):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    is_active = models.BooleanField()
    role = models.ForeignKey(Role, on_delete=models.PROTECT, default=1)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'role']

    def profile(self):
        profile = Profile.objects.get(user=self)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    verified = models.BooleanField(default=False)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

