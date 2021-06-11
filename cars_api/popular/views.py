from rest_framework.generics import ListAPIView

from .serializers import PopularCarsSerializer
from cars.models import Car


class PopularCarsListView(ListAPIView):
    serializer_class = PopularCarsSerializer

    def get_queryset(self):
        return Car.objects.all().order_by('-rates_number')
