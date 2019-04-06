from django.db import models
import random
import hashlib

class Sensor(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    description = models.TextField()
    secret_seed = models.CharField(max_length=10, editable=False)
    secret = models.CharField(max_length=60, editable=False)

    def save(self, *args, **kwargs):
        self.secret_seed = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(10))
        self.secret = hashlib.sha256(self.secret_seed).hexdigest()
        super(Sensor, self).save(*args, **kwargs)