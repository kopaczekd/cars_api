from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from cars.models import Car


class Rate(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1, message="Min rate is 1"), MaxValueValidator(5, message="Max rate is 5")])

    def __str__(self):
        return f'{self.car_id}, rate: {self.rating}'
