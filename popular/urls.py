from django.urls import path

from .views import PopularCarsListView

app_name = 'popular'

urlpatterns = [
    path('', PopularCarsListView.as_view(), name='list'),
]
