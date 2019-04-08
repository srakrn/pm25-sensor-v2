from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Reading, Sensor
import json
from json.decoder import JSONDecodeError


def index(request):
    return HttpResponse("It works!")


def api_request_latest(request, id):
    if request.method == "GET":
        reading = Reading.objects.filter(logged_by__id=id)
        data = serializers.serialize('json', reading)
        return HttpResponse(data, content_type="application/json")
    else:
        return HttpResponse(status=405)


@csrf_exempt
def api_log(request, id):
    if request.method == "POST":
        # Define a set of restricted fields
        # As `request.POST` can be accessed only once, this is needed.
        request_body = request.POST
        # Get a sensor with the requested ID. Return 404 if not found.
        try:
            sensor = Sensor.objects.get(id=id)
        except Sensor.DoesNotExist:
            return HttpResponse(status=404)
        # Check if the sensor's secret matches the requested secret
        try:
            if sensor.secret != request_body['secret']:
                return HttpResponse(status=403)
        except KeyError:
            return HttpResponse(status=403)
        reading_data = {f.name: request_body[f.name]
                        for f in Reading._meta.get_fields() if f.name in request_body and f.editable}
        logged_by = Sensor.objects.get(id=id)
        reading = Reading(**reading_data, logged_by=logged_by)
        reading.save()
        return JsonResponse(reading_data, status=200)
    else:
        # Return a 405 (method not allowed) code
        return HttpResponse(status=405)
