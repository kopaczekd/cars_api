from rest_framework.generics import ListCreateAPIView, DestroyAPIView

from .serializers import RateSerializer
from .models import Rate
from .tools import increase_rates_number

from .serializers import CarSerializer
from .models import Car


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarDeleteView(DestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_url_kwarg = 'id'


class RateListCreateView(ListCreateAPIView):
    serializer_class = RateSerializer
    queryset = Rate.objects.all()

    def perform_create(self, serializer):
        car_id = serializer.validated_data["car_id"].id
        increase_rates_number(car_id)
        serializer.save()
