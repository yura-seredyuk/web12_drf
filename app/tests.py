from copy import copy, deepcopy
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
        print(DATA)
        print(response.json())
        self.assertEqual(response.status_code, 201)

    def test_get_address(self):
        response = self.client.get(BASE_URL + "address/1")
        self.assertEqual(response.status_code, 200)

    def test_update_address(self):
        test_data = deepcopy(DATA)
        test_data["appartaments"] = 200
        response = self.client.put(BASE_URL + "address/1", data=test_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_address(self):
        response = self.client.delete(BASE_URL + "address/1")
        self.assertEqual(response.status_code, 204)

    def test_post_invalid_address(self):
        test_data = deepcopy(DATA)
        test_data["appartaments"] = 0
        response = self.client.post(BASE_URL + "address/", data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('cannot be less or equal zero', response.json()['non_field_errors'][0])
        print("Test 1. Passed")
        test_data["appartaments"] = -5
        response = self.client.post(BASE_URL + "address/", data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('cannot be less or equal zero', response.json()['non_field_errors'][0])
        print("Test 2. Passed")
        test_data["appartaments"] = "appartaments"
        response = self.client.post(BASE_URL + "address/", data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('valid integer is required', response.json()["appartaments"][0])
        print("Test 3. Passed")
        test_data["appartaments"] = DATA["appartaments"]
        test_data["country"] = "IO"
        response = self.client.post(BASE_URL + "address/", data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('must consists with more then 2 characters', response.json()["non_field_errors"][0])
        print("Test 4. Passed")
        test_data["country"] = "Country123"
        response = self.client.post(BASE_URL + "address/", data=test_data)
        self.assertEqual(response.status_code, 400)
        print("Test 5. Passed")





    def test_get_undefined_address(self):
        response = self.client.get(BASE_URL + "address/100")
        self.assertEqual(response.status_code, 404)

    def test_delete_undefined_address(self):
        response = self.client.delete(BASE_URL + "address/100")
        self.assertEqual(response.status_code, 404)

    def test_update_undefined_address(self):
        response = self.client.put(BASE_URL + "address/100")
        self.assertEqual(response.status_code, 404)
