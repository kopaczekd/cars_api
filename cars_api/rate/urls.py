from django.urls import path

from .views import RateListCreateView

app_name = 'rate'

urlpatterns = [
    path('', RateListCreateView.as_view(), name='rate_list_create')
]
