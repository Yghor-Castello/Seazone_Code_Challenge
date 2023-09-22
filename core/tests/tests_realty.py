from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.models.models_realty import Realty


class RealtyViewTestCase(APITestCase):
    """Test suite for the Realty view functionalities."""

    def setUp(self):
        """Set up test environment for the Realty view tests."""
        self.realty = Realty.objects.create(
            guest_limit=4,
            bathroom_count=2,
            accepts_pets=True,
            cleaning_fee=150.50,
            activation_date="2023-01-01"
        )
        self.url_list_create = reverse('realty-list')
        self.url_detail = reverse('realty-detail', args=[self.realty.code_realty])

    def test_list_realties(self):
        """Test listing all Realty objects."""
        response = self.client.get(self.url_list_create)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_realty(self):
        """Test retrieving a single Realty object by its unique code."""
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Update the attribute name to code_realty
        self.assertEqual(response.data['code_realty'], self.realty.code_realty)

    def test_create_realty(self):
        """Test creating a new Realty object."""
        data = {
            'guest_limit': 5,
            'bathroom_count': 3,
            'accepts_pets': False,
            'cleaning_fee': 175.00,
            'activation_date': '2023-02-01'
        }
        response = self.client.post(self.url_list_create, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Realty.objects.count(), 2)

    def test_update_realty(self):
        """Test updating an existing Realty object's attributes."""
        data = {
            'guest_limit': 5,
        }
        response = self.client.patch(self.url_detail, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.realty.refresh_from_db()
        self.assertEqual(self.realty.guest_limit, 5)

    def test_delete_realty(self):
        """Test deleting a Realty object."""
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Realty.objects.count(), 0)

    def test_create_realty_missing_fields(self):
        """Test creating a Realty object with missing non-required fields."""
        data = {
            'guest_limit': 5,
            'bathroom_count': 2,  
            'accepts_pets': True,  
            'cleaning_fee': 150.50,  
            'activation_date': '2023-02-01'  
        }
        response = self.client.post(self.url_list_create, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Realty.objects.count(), 2, f"Unexpected number of Realty objects. Expected 2 but found {Realty.objects.count()}.")