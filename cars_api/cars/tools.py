import requests


def does_car_exists(data):
    given_make = data["make"]
    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{given_make}?format=json'
    response = requests.get(url)
    count_of_models = response.json()['Count']
    if count_of_models > 0:
        models = response.json()['Results']
        given_model = data["model"]
        for model in models:
            if given_model == model['Model_Name']:
                return True
    return False
