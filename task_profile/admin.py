from django.contrib import admin
from .models import CustomerProfile, TaskerProfile, Notification

admin.site.register(TaskerProfile)
admin.site.register(Notification)
admin.site.register(CustomerProfile)

# Register your models here.
