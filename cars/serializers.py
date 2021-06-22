from django.db.models import Avg
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator

from rate.models import Rate
from .tools import does_car_exists
from .models import Car


class CarSerializer(ModelSerializer):
    avg_rating = SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'avg_rating']
        validators = [
            UniqueTogetherValidator(
                queryset=Car.objects.all(),
                fields=['make', 'model']
            )
        ]

    @staticmethod
    def get_avg_rating(obj):
        all_rates = Rate.objects.filter(car_id=obj.id)
        if all_rates:
            avg_rating_dict = all_rates.aggregate(Avg('rating'))
            avg_rating = round(avg_rating_dict['rating__avg'], 1)
            return avg_rating
        else:
            return 'No rates'

    def validate(self, data):
        if does_car_exists(data):
            return data
        else:
            raise ValidationError(detail="Car doesn't exist.")


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = ['car_id', 'rating']
