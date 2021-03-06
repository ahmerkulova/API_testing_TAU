import requests
from assertpy import assert_that
from lxml import etree

from config import COVID_TRACKER_HOST


def test_covid_cases_have_crossed_a_million():
    """ Test to assert XML element (found via XPath) to be <1M """
    response = requests.get(f'{COVID_TRACKER_HOST}/api/v1/summary/latest')
    response_xml = response.text

    """ XML response should to deserialized (string to python object) into a ElementTree object. 
    Need to provide fromstring() data in bytes format with UTF-8 encoding to avoid ValueError """
    xml_tree = etree.fromstring(bytes(response_xml, encoding='utf8'))
    total_cases = xml_tree.xpath('//data/summary/total_cases')[0].text

    assert_that(int(total_cases)).is_greater_than(1000000)


def test_covid_cases_sum_by_country_matches_total():
    """ Test to assert sum of country cases (found via XPath in a loop) matches overall sum """
    response = requests.get(f'{COVID_TRACKER_HOST}/api/v1/summary/latest')
    response_xml = response.text
    xml_tree = etree.fromstring(bytes(response_xml, encoding='utf8'))

    overall_cases = int(xml_tree.xpath("//data/summary/total_cases")[0].text)
    # Another way to specify XPath first and then use to evaluate on an XML tree
    search_for = etree.XPath("//data//regions//total_cases")
    cases_by_country = 0
    for region in search_for(xml_tree):
        cases_by_country += int(region.text)

    assert_that(overall_cases).described_as('No matching sums').is_equal_to(cases_by_country)
