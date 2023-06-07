import requests
import json

# SUGGESTIONS

# use datetime objects - pay attention to how they're formatted! 
# generate random values
# import geoJSON examples
# extend the function with inputs
# create loops with data


def send_request():
    # Request
    # POST http://127.0.0.1:8000/collector/

    try:
        response = requests.post(
            url="http://127.0.0.1:8000/collector/",
            headers={
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "end_time": "2022-11-18T09:30:00+00:00",
                "energy_used_kwh": 4,
                "end_battery_percent": 80,
                "distance_miles": 122,
                "start_time": "2022-11-18T09:00:00+00:00",
                "start_battery_percent": 99,
                "data": {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "properties": {

                            },
                            "geometry": {
                                "type": "LineString",
                                "coordinates": [
                                    [
                                        -3.8014582170991105,
                                        50.57206458537803
                                    ],
                                    [
                                        -2.7670795986162773,
                                        51.05393251988394
                                    ],
                                    [
                                        -1.8904875490539723,
                                        51.11450459220768
                                    ]
                                ]
                            }
                        }
                    ]
                }
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


send_request()