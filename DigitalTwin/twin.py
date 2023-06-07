import random
import requests
import json

# SUGGESTIONS

# use datetime objects - pay attention to how they're formatted! 
# generate random values
# import geoJSON examples
# extend the function with inputs
# create loops with data

numberOfTrips = 10

for x in range(numberOfTrips):

    rawData = '''{
                "end_time": "2022-11-12T05:30:00+00:00",
                "energy_used_kwh": 5,
                "end_battery_percent": 50,
                "distance_miles": 142,
                "start_time": "2022-11-18T05:00:00+00:00",
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
            }
 '''

    # random journy generaitor
    myData = json.loads(rawData) 

    print("_______START _______")

    distance = random.randint(10, 300)

    startBatterPercentage =  random.randint(50, 100)

    endBatteryPercentage = startBatterPercentage - distance/6

    energyUsed = (startBatterPercentage - endBatteryPercentage) / 5

    startLocation = [random.randint(1, 4)*-1, random.randint(50, 60)]

    lengthOfJourny = random.randint(10, 20)

    myTestjourny = [startLocation]

    for x in range(lengthOfJourny):
        direction = random.randint(0, 1)
        ditence = random.randint(2, 10)*0.001
        directionagain = random.choice((-1, 1))

        nextLocation = myTestjourny[x]

        nextLocation[direction] += ditence*directionagain

        myTestjourny.append([nextLocation[0], nextLocation[1]])


    myData['data']['features'][0]['geometry']['coordinates'] = myTestjourny
    myData['energy_used_kwh'] = energyUsed
    myData['end_battery_percent'] = endBatteryPercentage
    myData['distance_miles'] = distance
    myData['start_battery_percent'] = startBatterPercentage

    def send_request():
        # Request
        # POST http://127.0.0.1:8000/collector/

        try:
            proxies = {
                "http": "",
                "https": "",
            }
            response = requests.post(
                url="http://127.0.0.1:8000/collector/",
                headers={
                    "Content-Type": "application/json; charset=utf-8",
                },
                data=json.dumps(myData), 
                proxies=proxies
            )
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')
    send_request()