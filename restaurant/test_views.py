from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Menu, Booking


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title='Pasta', price=15.00, inventory=20)

    def test_get_menu_items(self):
        response = self.client.get('/api/menu-items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Pasta')


class BookingViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Booking.objects.create(first_name='Layan', reservation_date='2026-05-03', reservation_slot=18)

    def test_get_bookings(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Layan')

    def test_create_booking(self):
        data = {
            'first_name': 'Hala',
            'reservation_date': '2026-05-04',
            'reservation_slot': 19,
        }
        response = self.client.post('/api/bookings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)
