import pytest
from faker import Faker

from utils.file_reader import read_file


@pytest.fixture
def create_data():
    payload = read_file('create_person.json')
    f = Faker()

    last_name = f'{payload["lname"]} number {f.pyint()}'
    payload['lname'] = last_name

    yield payload
    print(f'\nData prepared: {payload["fname"]} is name, {payload["lname"]} is last name')
