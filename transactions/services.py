import random
from functools import reduce

import requests
from rest_framework import status


class JokeService:
    request_params = {
        "chuck": {
            "url": "https://api.chucknorris.io/jokes/random",
            "field": "value"
        },
        "dad": {
            "url": "https://icanhazdadjoke.com/",
            "field": "joke"
        }
    }

    headers = {"Content-Type": "json", "Accept": "application/json"}

    def __init__(self, joke_type):
        self.__joke_type = joke_type
        if self.__joke_type == "random":
            random_option = self.random_option()
            self.request_params["random"] = self.request_params[random_option]

    def get_joke(self):
        try:
            request_param = self.request_params[self.__joke_type]
            response = requests.get(request_param["url"], headers=self.headers)
            if response.status_code != status.HTTP_200_OK:
                return None
            return response.json()[request_param["field"]]
        except Exception as ex:
            print("Exception -> {}".format(ex))
            return None

    @staticmethod
    def random_option():
        random_key = ["chuck", "dad"]
        random_number = random.randint(0, 1)
        return random_key[random_number]


class LowestCommonMultipleService:

    def __init__(self, numbers):
        self.__numbers = numbers

    @property
    def list_numbers(self):
        return self.__numbers

    @list_numbers.setter
    def list_numbers(self, numbers):
        self.__numbers = numbers

    @staticmethod
    def calculate(first_number, second_number):
        if first_number > second_number:
            greater_than = first_number
        else:
            greater_than = second_number
        while True:
            if greater_than % first_number == 0 and greater_than % second_number == 0:
                mcm = greater_than
                break
            greater_than += 1
        return mcm

    def parse_list(self):
        try:
            return list(map(lambda element: int(element), self.__numbers))
        except Exception as ex:
            print("Exception -> ".format(ex))
            return None

    def lowest_common_multiple(self):
        try:
            return reduce(
                lambda first_number, second_number: self.calculate(first_number, second_number),
                self.__numbers
            )
        except Exception as ex:
            print("Exception -> ".format(ex))
            return None


class ReturnPlusOneService:
    def __init__(self, number):
        self.__number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new_number):
        self.__number = new_number

    def parse_number(self):
        try:
            return int(self.__number)
        except Exception as ex:
            print("Exception -> ".format(ex))
            return None

    def add_one(self):
        return self.__number + 1
