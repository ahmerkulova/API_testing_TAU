import requests
import pytest
from assertpy.assertpy import assert_that, soft_assertions
from config import BASE_URI

from faker import Faker
from json import dumps, loads
from jsonpath_ng import parse
from cerberus import Validator

from utils.file_reader import *


@pytest.fixture
def create_data():
    payload = read_file('create_person.json')
    f = Faker()

    last_name = f'{payload["lname"]} number {f.pyint()}'
    payload['lname'] = last_name

    yield payload
    print(f'\nData prepared: {payload["fname"]} is name, {payload["lname"]} is last name')


def create_new_person(body=None):
    """ Function to create new user. json.dumps() is used to convert python dict to json string
     uuid4.uuid4 is used to get a unique last name to ensure we don’t have conflicting data """
    if body is None:
        f = Faker()
        unique_first_name = f.first_name()
        unique_last_name = f.last_name()
        payload = dumps({
            'fname': unique_first_name,
            'lname': unique_last_name
        })
    else:
        unique_first_name = body['fname']
        unique_last_name = body['lname']
        payload = dumps(body)

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post(url=BASE_URI, data=payload, headers=headers)
    assert_that(response.status_code, description='Person not created').is_equal_to(requests.codes.no_content)
    return unique_last_name


def search_created_user_in(peoples, last_name):
    """ Function to return bool of there is new user in the list of users """
    return [person for person in peoples if person['lname'] == last_name]
