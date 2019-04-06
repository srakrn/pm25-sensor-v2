from django.contrib import admin
from .models import Sensor, Reading

# Register your models here.
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'latitude', 'longitude']
    readonly_fields = ['secret']

admin.site.register(Sensor, SensorAdmin)

class ReadingAdmin(admin.ModelAdmin):
    list_display = ['logged_by', 'time']
    readonly_fields = ['time']

admin.site.register(Reading, ReadingAdmin)