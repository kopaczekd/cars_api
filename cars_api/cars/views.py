from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .serializers import CarSerializer
from .models import Car


class CarListView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarDeleteView(DestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_url_kwarg = 'id'
