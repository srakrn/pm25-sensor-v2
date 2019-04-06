from django.db import models
import random
import hashlib
import string

class Sensor(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    description = models.TextField()
    secret = models.CharField(max_length=60, editable=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Sensor at " + self.name

    def save(self, *args, **kwargs):
        secret_seed = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(10)) + str(self.id)
        self.secret = hashlib.sha256(secret_seed.encode('utf-8')).hexdigest()
        super(Sensor, self).save(*args, **kwargs)