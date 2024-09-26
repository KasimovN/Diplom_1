import random
import string


class Helper:
    @staticmethod
    def random_name(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def random_price(max_price):
        return round(random.uniform(0, max_price), 2)

    @staticmethod
    def random_ingredient_type(ingredient_types):
        return random.choice(ingredient_types)
