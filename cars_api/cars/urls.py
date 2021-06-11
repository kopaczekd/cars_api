from django.urls import path

from .views import CarListCreateView, CarDeleteView

app_name = 'cars'

urlpatterns = [
    path('', CarListCreateView.as_view(), name='car_list_create'),
    path('<int:id>/', CarDeleteView.as_view(), name='car_delete'),
]
