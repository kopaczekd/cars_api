from rest_framework.generics import ListCreateAPIView, DestroyAPIView, ListAPIView
from django.views.generic import TemplateView

from .serializers import CarSerializer, RateSerializer, PopularCarsSerializer
from .models import Rate, Car
from .tools import increase_rates_number


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


class PopularCarsListView(ListAPIView):
    serializer_class = PopularCarsSerializer

    def get_queryset(self):
        return Car.objects.all().order_by('-rates_number')


class IndexView(TemplateView):
    template_name = "index.html"
