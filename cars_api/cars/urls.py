from django.urls import path
from .views import CarListView, CarDeleteView

app_name = 'cars'

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('<int:id>/', CarDeleteView.as_view(), name='car_delete'),
]
