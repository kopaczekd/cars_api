from django.urls import path

from .views import CarListCreateView, CarDeleteView, RateListCreateView

app_name = 'cars'

urlpatterns = [
    # path('', ),
    path('cars/', CarListCreateView.as_view(), name='cars_list_create'),
    path('cars/<int:id>/', CarDeleteView.as_view(), name='cars_delete'),
    path('rate/', RateListCreateView.as_view(), name='rate_list_create'),
    # path('popular/', include('popular.urls')),
]
