from rest_framework import status
from rest_framework.test import APITestCase
from django.test.client import RequestFactory
from customer.models import Customer



class CustomerTest(APITestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_create_customer(self):
        """
        Ensure we can create a new customer object.
        """
        url = ('http://127.0.0.1:8000/customers/')
        data = {
            "id": 112,
            "name": "TestCase",
            "email": "TestCase",
            "phone": "12241241"
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'TestCase')
