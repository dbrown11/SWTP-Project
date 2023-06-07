from datetime import datetime
import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from swtp_project.users.models import Car, User, Journey

@csrf_exempt
@require_http_methods("POST")
def test_collector(request):
    body = json.loads(request.body)
    print(body)

    journey = Journey()

    journey.user = User.objects.all()[0]
    journey.car = Car.objects.all()[0]

    journey.distance_miles = body['distance_miles']
    journey.energy_used_kwh = body['energy_used_kwh']
    journey.start_time = body['start_time']
    journey.end_time = body['end_time']
    journey.start_battery_percent = body['start_battery_percent']
    journey.end_battery_percent = body['end_battery_percent']

    journey.data = body['data']

    journey.save()

    return JsonResponse({'response':journey.id})