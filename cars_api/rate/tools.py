from cars.models import Car


def increase_rates_number(car_id):
    car = Car.objects.get(id=car_id)
    car.rates_number += 1
    car.save()
