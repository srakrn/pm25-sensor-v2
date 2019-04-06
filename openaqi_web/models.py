from django.db import models
import random
import hashlib
import string


class Sensor(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=12, decimal_places=6)
    longitude = models.DecimalField(max_digits=12, decimal_places=6)
    description = models.TextField()
    secret = models.CharField(max_length=20, editable=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Sensor at " + self.name

    def save(self, *args, **kwargs):
        self.secret = ''.join(random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(20))
        super(Sensor, self).save(*args, **kwargs)


class Reading(models.Model):
    logged_by = models.ForeignKey(Sensor, models.CASCADE)
    pm_10 = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="PM10", blank=True, null=True)
    pm_25 = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="PM2.5", blank=True, null=True)
    pm_1 = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="PM1", blank=True, null=True)
    temperature = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    humidity = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Reading from " + self.logged_by.name + " at " + self.time.strftime("%m/%d/%Y, %H:%M")
