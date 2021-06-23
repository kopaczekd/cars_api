import requests
from rest_framework.exceptions import APIException

from cars.models import Car


def does_car_exists(data):
    given_make = data["make"]
    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{given_make}?format=json'
    try:
        response = requests.get(url)
        count_of_models = response.json()['Count']
        if count_of_models > 0:
            models = response.json()['Results']
            given_model = data["model"].lower()
            for model in models:
                if given_model == model['Model_Name'].lower():
                    return True
    except:
        raise APIException("Something went wrong with external API")
    return False


def increase_rates_number(car_id):
    car = Car.objects.get(id=car_id)
    car.rates_number += 1
    car.save()
