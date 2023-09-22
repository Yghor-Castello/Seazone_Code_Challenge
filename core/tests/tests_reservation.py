from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from core.models import Reservation, Advertisement, Realty


class ReservationViewTestCase(TestCase):
    """
    Test cases for the Reservation views.
    """

    def setUp(self):
        """
        Set up test data.
        """
        self.client = APIClient()

        self.realty = Realty.objects.create(
            code_realty="R123456",
            guest_limit=4,
            bathroom_count=2,
            accepts_pets=True,
            cleaning_fee="50.00",
            activation_date="2023-01-01"
        )

        self.advertisement = Advertisement.objects.create(
            realty=self.realty,
            platform_name="TestPlatform",
            platform_fee="10.00"
        )

        self.reservation_data = {
            'code_reservation': "ADV0008",
            'advertisement': self.advertisement.id,
            'checkin_date': '2023-10-01',
            'checkout_date': '2023-10-10',
            'total_price': '1000.00',
            'comment': "Bla Bla",
            'guest_count': 2
        }

    def test_list_reservations(self):
        """
        Test the endpoint for listing reservations.
        """
        url = reverse('reservation-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_checkin_date_after_checkout_date(self):
        """
        Test creating a reservation with a check-in date after the checkout date.
        """
        self.reservation_data['checkin_date'] = '2023-10-10'
        self.reservation_data['checkout_date'] = '2023-10-01'
        url = reverse('reservation-list')
        response = self.client.post(url, self.reservation_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], "Check-in date cannot be after or the same as the check-out date.")

    def test_checkin_date_same_as_checkout_date(self):
        """
        Test creating a reservation with a check-in date the same as the checkout date.
        """
        self.reservation_data['checkin_date'] = '2023-10-10'
        self.reservation_data['checkout_date'] = '2023-10-10'
        url = reverse('reservation-list')
        response = self.client.post(url, self.reservation_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], "Check-in date cannot be after or the same as the check-out date.")

    def test_update_reservation_disabled(self):
        """
        Test attempting to update a reservation (PUT method), which should be disabled.
        """
        self.reservation_data['advertisement'] = self.advertisement
        reservation = Reservation.objects.create(**self.reservation_data)
        url = reverse('reservation-detail', args=[reservation.id])
        response = self.client.put(url, {'comment': 'Updated comment'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)