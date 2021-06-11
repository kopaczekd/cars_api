from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from cars.models import Car


class PopularAPITests(APITestCase):
    def setUp(self):
        url_list_create_rate = reverse('rate:list_create')
        self.car_1 = Car.objects.create(make='Lamborghini', model='Gallardo')
        data_1 = {
            'car_id': self.car_1.id,
            'rating': 5
        }
        self.client.post(url_list_create_rate, data_1)
        self.client.post(url_list_create_rate, data_1)
        self.client.post(url_list_create_rate, data_1)
        self.car_2 = Car.objects.create(make='Lamborghini', model='Aventador')
        data_2 = {
            'car_id': self.car_2.id,
            'rating': 5
        }
        self.client.post(url_list_create_rate, data_2)
        self.client.post(url_list_create_rate, data_2)
        self.client.post(url_list_create_rate, data_2)
        self.client.post(url_list_create_rate, data_2)
        self.client.post(url_list_create_rate, data_2)

    def test_taking_all_popular_cars(self):
        url_popular = reverse('popular:list')
        response = self.client.get(url_popular)
        self.assertEqual(response.data[0]['id'], self.car_2.id)
        self.assertEqual(response.data[0]['rates_number'], 5)
        self.assertEqual(response.data[1]['id'], self.car_1.id)
        self.assertEqual(response.data[1]['rates_number'], 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
