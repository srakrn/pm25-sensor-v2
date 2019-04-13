from django.db import models
import random
import hashlib
import string
from itertools import chain


def model_to_dict(instance, fields=None, exclude=None, hide_non_editable=True):
    """
    Return a dict containing the data in ``instance`` suitable for passing as
    a Form's ``initial`` keyword argument.

    ``fields`` is an optional list of field names. If provided, return only the
    named.

    ``exclude`` is an optional list of field names. If provided, exclude the
    named from the returned dict, even if they are listed in the ``fields``
    argument.

    ``hide_non_editable`` is an optional boolean. If set to True, the non-editable
    fields are returned.
    """
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):
        if hide_non_editable and not getattr(f, 'editable', False):
            continue
        if fields and f.name not in fields:
            continue
        if exclude and f.name in exclude:
            continue
        data[f.name] = f.value_from_object(instance)
    return data


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
    id = models.AutoField(primary_key=True, editable=False)
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
    time = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "Reading from " + self.logged_by.name + " at " + self.time.strftime("%m/%d/%Y, %H:%M")
