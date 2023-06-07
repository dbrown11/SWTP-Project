from django.shortcuts import render
from django.http import JsonResponse
import json

from swtp_project.users.models import Journey

def render_map(request):
    return render(request, 'map.html', {})


def render_geojson(request):

    journey_list = Journey.objects.all()

    return_data = {
                    "type": "FeatureCollection",
                    "features": []
    }

    for journey in journey_list:
        return_data["features"] += journey.data['features']

    return JsonResponse(return_data)