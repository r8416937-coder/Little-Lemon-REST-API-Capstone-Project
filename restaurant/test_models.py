from django.test import TestCase
from .models import Menu, Booking

class MenuModelTest(TestCase):
    def test_menu_string(self):
        item = Menu.objects.create(title='Greek Salad', price=12.99, inventory=10)
        self.assertEqual(str(item), 'Greek Salad')

class BookingModelTest(TestCase):
    def test_booking_string(self):
        booking = Booking.objects.create(first_name='Maryam', reservation_date='2026-05-03', reservation_slot=12)
        self.assertIn('Maryam', str(booking))
