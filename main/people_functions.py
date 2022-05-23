import requests
from assertpy.assertpy import assert_that, soft_assertions
from config import BASE_URI

from faker import Faker
from json import dumps


def create_new_person():
    """ Function to create new user. json.dumps() is used to convert python dict to json string
     uuid4.uuid4 is used to get a unique last name to ensure we don’t have conflicting data """
    f = Faker()
    unique_first_name = f.first_name()
    unique_last_name = f.last_name()
    payload = dumps({
        'fname': unique_first_name,
        'lname': unique_last_name
    })
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
