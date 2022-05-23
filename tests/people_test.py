import requests
from assertpy.assertpy import assert_that
from config import BASE_URI


def test_read_all_has_kent():
    """ Function to assert that in response of GET request one of first names contains 'Kent' """
    response = requests.get(BASE_URI)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    response_text = response.json()
    first_names = [people['fname'] for people in response_text]
    assert_that(first_names).contains('Kent')
