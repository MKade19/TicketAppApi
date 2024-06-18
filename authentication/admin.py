from django.contrib import admin
from .models import User, Profile, Role

class UserAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email']
    search_fields = ['fullname', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user', 'full_name' ,'verified']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Role)
