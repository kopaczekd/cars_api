from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator
from .tools import does_car_exists
from .models import Car


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model']
        validators = [
            UniqueTogetherValidator(
                queryset=Car.objects.all(),
                fields=['make', 'model']
            )
        ]

    def validate(self, data):
        if does_car_exists(data):
            return data
        else:
            raise ValidationError(detail="Car doesn't exist.")
