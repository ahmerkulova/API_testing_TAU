from main.people_functions import *


def test_read_all_has_kent():
    """ Test to assert that one of first names in response of GET request contains 'Kent' """
    response = requests.get(BASE_URI)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    response_text = response.json()
    first_names = [people['fname'] for people in response_text]
    assert_that(first_names).contains('Kent')


def test_new_person_can_be_added():
    """ Test to assert that new added user can be found in the list of users """
    unique_last_name = create_new_person()
    peoples = requests.get(BASE_URI).json()
    is_new_user_created = search_created_user_in(peoples, unique_last_name)
    assert_that(is_new_user_created).is_not_empty()




