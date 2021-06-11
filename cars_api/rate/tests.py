from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from cars.models import Car
from rate.models import Rate


class RateAPITest(APITestCase):
    def setUp(self):
        self.car = Car.objects.create(make='Lamborghini', model='Gallardo')
        self.url_list_create = reverse('rate:list_create')
        Rate.objects.create(car_id=self.car, rating=5)

    def test_rate_creation_success(self):
        data = {
            'car_id': self.car.id,
            'rating': 5
        }
        response = self.client.post(self.url_list_create, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_rate_creation_failure_wrong_rating(self):
        data = {
            'car_id': self.car.id,
            'rating': 6
        }
        response = self.client.post(self.url_list_create, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rate_creation_failure_wrong_car_id(self):
        data = {
            'car_id': 777,
            'rating': 5
        }
        response = self.client.post(self.url_list_create, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_taking_all_rates(self):
        response = self.client.get(self.url_list_create)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
