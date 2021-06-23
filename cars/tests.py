from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
import requests

from .models import Car, Rate
from .tools import does_car_exists


class CarAPITest(APITestCase):
    def setUp(self):
        self.url_list_create = reverse('cars:cars_list_create')
        self.car = Car.objects.create(make='Lamborghini', model='Gallardo')
        Car.objects.create(make='Volkswagen', model='Passat')

    def test_car_creation_success(self):
        data = {
            'make': 'Volkswagen',
            'model': 'Golf'
        }
        response = self.client.post(self.url_list_create, data)
        self.assertEqual(response.data['make'], data['make'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_car_creation_failure(self):
        data = {
            'make': 'Volkswagennn',
            'model': 'Golf'
        }
        response = self.client.post(self.url_list_create, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_taking_all_cars(self):
        response = self.client.get(self.url_list_create)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_car_deletion_success(self):
        response_get_before_deletion = self.client.get(self.url_list_create)
        self.assertEqual(len(response_get_before_deletion.data), 2)
        first_car_id = response_get_before_deletion.data[0]['id']
        url_delete = reverse('cars:cars_delete', args=[first_car_id])
        response_deletion = self.client.delete(url_delete)
        self.assertEqual(response_deletion.status_code, status.HTTP_204_NO_CONTENT)
        response_get_after_deletion = self.client.get(self.url_list_create)
        self.assertEqual(len(response_get_after_deletion.data), 1)

    def test_car_deletion_failure(self):
        url_delete = reverse('cars:cars_delete', args=[777])
        response_deletion = self.client.delete(url_delete)
        self.assertEqual(response_deletion.status_code, status.HTTP_404_NOT_FOUND)

    def test_calculating_avg_rating(self):
        Rate.objects.create(car_id=self.car, rating=5)
        Rate.objects.create(car_id=self.car, rating=4)
        response = self.client.get(self.url_list_create)
        for car in response.data:
            if car['id'] == self.car:
                self.assertEqual(car['avg_rating'], 4.5)


class PopularAPITests(APITestCase):
    def setUp(self):
        url_list_create_rate = reverse('cars:rate_list_create')
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
        url_popular = reverse('cars:popular_list')
        response = self.client.get(url_popular)
        self.assertEqual(response.data[0]['id'], self.car_2.id)
        self.assertEqual(response.data[0]['rates_number'], 5)
        self.assertEqual(response.data[1]['id'], self.car_1.id)
        self.assertEqual(response.data[1]['rates_number'], 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RateAPITest(APITestCase):
    def setUp(self):
        self.car = Car.objects.create(make='Lamborghini', model='Gallardo')
        self.url_list_create = reverse('cars:rate_list_create')
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


class TestExternalAPI(TestCase):
    def test_connection(self):
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/Lamborghini?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DoesCarExistsMethodTests(TestCase):
    def test_car_exists(self):
        data = {
            'make': 'Lamborghini',
            'model': 'Aventador'
        }
        self.assertTrue(does_car_exists(data))

    def test_car_doesnt_exists(self):
        data = {
            'make': 'Lamborghini',
            'model': 'no-model'
        }
        self.assertFalse(does_car_exists(data))
