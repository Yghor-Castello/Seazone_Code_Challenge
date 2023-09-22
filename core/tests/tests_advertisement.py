import datetime

from decimal import Decimal
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.models.models_realty import Realty
from core.models.models_advertisement import Advertisement


class AdvertisementViewTestCase(APITestCase):
    """
    Test cases for the Advertisement views.
    """

    def setUp(self):
        """
        Set up test data.
        """
        self.realty = Realty.objects.create(
            guest_limit=4,
            bathroom_count=2,
            accepts_pets=True,
            cleaning_fee=150.50,
            activation_date="2023-01-01"
        )
        self.url_list_create = reverse('realty-list')
        self.url_detail = reverse('realty-detail', args=[self.realty.code_realty])

    def test_list_advertisements(self):
        """
        Test the endpoint for listing advertisements.
        """
        url = reverse('advertisement-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_advertisement(self):
        """
        Test creating a new advertisement.
        """
        realty = Realty.objects.create(
            code_realty="CODE123",
            guest_limit=5,
            bathroom_count=2,
            accepts_pets=True,
            cleaning_fee=Decimal("50.00"),
            activation_date=datetime.date.today()
        )

        data = {
            'realty': realty.id,
            'platform_name': "Some Platform",
            'platform_fee': "100.50"
        }

        url = reverse('advertisement-list')
        response = self.client.post(url, data, format='json')

    def test_update_advertisement(self):
        """
        Test updating an existing advertisement.
        """
        advertisement = Advertisement.objects.create(
            realty=self.realty,
            platform_name='ExamplePlatform',
            platform_fee=100.00,
        )
        url = reverse('advertisement-detail', args=[advertisement.pk])
        data = {
            'platform_name': 'UpdatedPlatform',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        advertisement.refresh_from_db()
        self.assertEqual(advertisement.platform_name, 'UpdatedPlatform')

    def test_delete_advertisement(self):
        """
        Test deleting an advertisement.
        """
        advertisement = Advertisement.objects.create(
            realty=self.realty,
            platform_name='ExamplePlatform',
            platform_fee=100.00,
        )
        url = reverse('advertisement-detail', args=[advertisement.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        if response.status_code != status.HTTP_405_METHOD_NOT_ALLOWED:
            print(response.data)