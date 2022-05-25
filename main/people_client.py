from json import dumps
from faker import Faker

from main.base_client import BaseClient
from utils.request import APIRequest
from config import BASE_URI


class PeopleClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = BASE_URI
        self.request = APIRequest()

    def create_user(self, body=None):
        last_name, response = self.__create_unique_user(body)
        return last_name, response

    def __create_unique_user(self, body=None):
        """ Private method to create new user. json.dumps() is used to convert dict to json string
        Faker is used to get a unique last name to ensure we don’t have conflicting data """
        if body is None:
            f = Faker()
            first_name = f.first_name()
            last_name = f.last_name()
            payload = dumps({
                'fname': first_name,
                'lname': last_name
            })
        else:
            last_name = body['lname']
            payload = dumps(body)

        response = self.request.post(self.base_url, payload, self.headers)
        return last_name, response

    def read_one_person_by_id(self, person_id):
        pass

    def read_all_persons(self):
        return self.request.get(self.base_url)

    def update_person(self):
        pass

    def delete_person(self, person_id):
        url = f'{BASE_URI}/{person_id}'
        return self.request.delete(url)
