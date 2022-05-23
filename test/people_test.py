from main.people_functions import *


def test_read_all_has_kent():
    """ Test to assert that one of first names in response of GET request contains 'Kent' """
    response = requests.get(BASE_URI)
    with soft_assertions():
        assert_that(response.status_code, description='Person not created').is_equal_to(requests.codes.ok)
        response_text = response.json()
        assert_that(response_text).described_as('No matching names').extracting('fname').is_not_empty().contains('Kent')


def test_new_person_can_be_added():
    """ Test to assert that new added user (POST method) can be found in the list of users """
    unique_last_name = create_new_person()
    peoples = requests.get(BASE_URI).json()
    is_new_user_created = search_created_user_in(peoples, unique_last_name)
    assert_that(is_new_user_created).is_not_empty()


def test_created_person_can_be_deleted():
    """ Test to assert that new added can be deleted (DELETE method) """
    persons_last_name = create_new_person()
    peoples = requests.get(BASE_URI).json()
    newly_created_user = search_created_user_in(peoples, persons_last_name)[0]
    delete_url = f'{BASE_URI}/{newly_created_user["person_id"]}'
    response = requests.delete(delete_url)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)


def test_person_can_be_added_with_a_json_template(create_data):
    create_new_person(create_data)

    response = requests.get(BASE_URI)
    peoples = loads(response.text)

    # Get all last names for any object in the root array
    # Here $ = root, [*] represents any element in the array
    # Read full syntax: https://pypi.org/project/jsonpath-ng/
    jsonpath_expr = parse("$.[*].lname")
    result = [match.value for match in jsonpath_expr.find(peoples)]

    expected_last_name = create_data['lname']
    assert_that(result).contains(expected_last_name)
