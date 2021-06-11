from rest_framework.generics import ListCreateAPIView

from rate.serializers import RateSerializer
from rate.models import Rate


class RateListCreateView(ListCreateAPIView):
    serializer_class = RateSerializer
    queryset = Rate.objects.all()
