from django.contrib import admin
from .models import Sensor

# Register your models here.
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Sensor, SensorAdmin)