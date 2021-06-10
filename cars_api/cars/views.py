from rest_framework.generics import ListCreateAPIView
from .serializers import CarSerializer
from .models import Car


class CarListView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
