import requests
from assertpy.assertpy import assert_that
from config import BASE_URI

from json import dumps
from uuid import uuid4


def create_new_person():
    """ Function to create new user. json.dumps() is used to convert python dict to json string
     uuid4.uuid4 is used to get a unique last name to ensure we don’t have conflicting data """
    unique_last_name = f'User {str(uuid4())}'
    payload = dumps({
        'fname': 'New',
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
