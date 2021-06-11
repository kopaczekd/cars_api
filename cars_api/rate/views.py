from rest_framework.generics import ListCreateAPIView

from .serializers import RateSerializer
from .models import Rate
from .tools import increase_rates_number


class RateListCreateView(ListCreateAPIView):
    serializer_class = RateSerializer
    queryset = Rate.objects.all()

    def perform_create(self, serializer):
        car_id = serializer.validated_data["car_id"].id
        increase_rates_number(car_id)
        serializer.save()
