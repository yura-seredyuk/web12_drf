from urllib import response
import requests
from pprint import pprint


BASE_URL = 'http://127.0.0.1:8000/'
def get_adresses():
    response = requests.get(BASE_URL+'address_list/')
    print(response.json(), "\n\tstatus_code:", response.status_code)

def get_adresses_():
    response = requests.get(BASE_URL+'address/')
    print(response.json(), "\n\tstatus_code:", response.status_code)

def get_special_adress():
    response = requests.get(BASE_URL+'address_list/1')
    print(response.json(), "\n\tstatus_code:", response.status_code)


def post_special_adress():
    data = {
        'appartaments': 4254,
        'city': 'New York',
        'country': 'USA',
        'house_num': '33',
        'street': 'Freedom',
        'zip_code': 33027
    }
    response = requests.post(BASE_URL+'address_list/', data=data)
    print(response.json(), "\n\tstatus_code:", response.status_code)


def put_special_adress():
    data = {
        'id':4,
        'appartaments': 1,
        'city': 'New York',
        'country': 'USA',
        'house_num': '1',
        'street': 'Freedom',
        'zip_code': 33027
    }
    response = requests.put(BASE_URL+'address_list/6/', data=data)
    print(response.json(), "\n\tstatus_code:", response.status_code)

def put_special_adress_():
    data = {
        'id':8,
        'appartaments': 0,
        'city': 'New York',
        'country': 'USA',
        'house_num': '12',
        'street': 'Freedom',
        'zip_code': 33027
    }
    response = requests.put(BASE_URL+'address/8', data=data)
    print(response.json(), "\n\tstatus_code:", response.status_code)

def delete_special_adress():
    response = requests.delete(BASE_URL+'address_list/5')
    print(response, "\n\tstatus_code:", response.status_code)


if __name__ == "__main__":
    # get_adresses()
    # get_special_adress()
    # post_special_adress()
    # put_special_adress()
    # get_adresses_()
    put_special_adress_()
    # delete_special_adress()
    pass