from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Car
from rate.models import Rate


class CarAPITest(APITestCase):
    def setUp(self):
        self.url_list_create = reverse('cars:list_create')
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
        url_delete = reverse('cars:delete', args=[first_car_id])
        response_deletion = self.client.delete(url_delete)
        self.assertEqual(response_deletion.status_code, status.HTTP_204_NO_CONTENT)
        response_get_after_deletion = self.client.get(self.url_list_create)
        self.assertEqual(len(response_get_after_deletion.data), 1)

    def test_car_deletion_failure(self):
        url_delete = reverse('cars:delete', args=[777])
        response_deletion = self.client.delete(url_delete)
        self.assertEqual(response_deletion.status_code, status.HTTP_404_NOT_FOUND)

    def test_calculating_avg_rating(self):
        Rate.objects.create(car_id=self.car, rating=5)
        Rate.objects.create(car_id=self.car, rating=4)
        response = self.client.get(self.url_list_create)
        for car in response.data:
            if car['id'] == self.car:
                self.assertEqual(car['avg_rating'], 4.5)