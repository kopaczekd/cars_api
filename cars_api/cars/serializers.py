from rest_framework.serializers import ModelSerializer
from .models import Car


class CarsSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ['make', 'model']
