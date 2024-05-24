from django.contrib import admin
from .models import Event, Application, ApplicationSeat

admin.site.register(Event)
admin.site.register(Application)
admin.site.register(ApplicationSeat)