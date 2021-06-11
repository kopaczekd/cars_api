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
