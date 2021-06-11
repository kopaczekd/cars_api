from rest_framework.serializers import ModelSerializer

from rate.models import Rate


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = ['car_id', 'rating']
