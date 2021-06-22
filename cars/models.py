from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Car(models.Model):
    make = models.CharField(
        max_length=255
    )
    model = models.CharField(
        max_length=255
    )
    rates_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.id} - {self.make} {self.model}'


class Rate(models.Model):
    car_id = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='car_ids')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1, message="Min rate is 1"), MaxValueValidator(5, message="Max rate is 5")])

    def __str__(self):
        return f'{self.car_id}, rate: {self.rating}'
