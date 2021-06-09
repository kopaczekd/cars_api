from rest_framework.generics import ListAPIView
from .serializers import CarsSerializer
from .models import Car


class CarListView(ListAPIView):
    serializer_class = CarsSerializer
    queryset = Car.objects.all()
