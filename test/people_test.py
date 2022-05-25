import requests

from main.people_client import PeopleClient
from test.helpers.people_helpers import *
from test.helpers.people_assertions import *

client = PeopleClient()


def test_read_all_has_kent():
    """ Test to assert that one of first names in response of GET request contains 'Kent' """
    response = client.read_all_persons()

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_people_have_person_with_first_name(response, first_name='Kent')


def test_new_person_can_be_added():
    """ Test to assert that new added user (POST method) can be found in the list of users """
    last_name, response = client.create_person()
    assert_that(response.status_code, description='Person not created').is_equal_to(requests.codes.no_content)

    people = client.read_all_persons().as_dict
    is_new_user_created = search_created_user_in(people, last_name)
    assert_person_is_present(is_new_user_created)


def test_created_person_can_be_deleted():
    """ Test to assert that new added can be deleted (DELETE method) """
    persons_last_name, _ = client.create_person()

    people = client.read_all_persons().as_dict
    new_person_id = search_created_user_in(people, persons_last_name)['person_id']

    response = client.delete_person(new_person_id)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)


def test_person_can_be_added_with_a_json_template(create_data):
    """ Test to assert user data can be parsed from .json and user can be added """
    client.create_person(create_data)

    response = client.read_all_persons()
    peoples = response.as_dict

    """ $ = root, [*] = any element in the array (jsonpath-ng syntax)
        Get regex to find certain key values """
    result = search_nodes_using_json_path(peoples, json_path="$.[*].lname")

    expected_last_name = create_data['lname']
    assert_that(result).contains(expected_last_name)
