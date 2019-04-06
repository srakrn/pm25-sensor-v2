from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from .models import Reading, Sensor
import json
from json.decoder import JSONDecodeError


def index(request):
    return HttpResponse("It works!")


@csrf_exempt
def api_log(request, id):
    if request.method == "POST":
        try:
            sensor = Sensor.objects.get(secret=secret)
        except Sensor.DoesNotExist:
            return HttpResponse(status=404)
        data = request.body.decode('utf-8')
        return JsonResponse(request.POST, status=200)
    else:
        # Return a 405 (method not allowed) code
        return HttpResponse(status=405)
