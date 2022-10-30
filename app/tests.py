from urllib import response
from django.test import TestCase
from rest_framework.test import APITestCase, RequestsClient


BASE_URL = 'http://127.0.0.1:8000/'
DATA = {
    'appartaments': 999,
    'city': 'New York',
    'country': 'USA',
    'house_num': '99',
    'street': 'Freedom',
    'zip_code': 99999
}
class API_Testing(APITestCase):
    """
    """
    def setUp(self):
        self.client = RequestsClient()
        response = self.client.post(BASE_URL + "address/", data=DATA)
    
    def test_get_addresses(self):
        response = self.client.get(BASE_URL + "address/")
        # print(response.json())
        self.assertEqual(response.status_code, 200)


    def test_post_address(self):
        response = self.client.post(BASE_URL + "address/", data=DATA)
        # print(response.json())
        self.assertEqual(response.status_code, 201)
