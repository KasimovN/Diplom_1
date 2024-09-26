from helper import Helper


class StarBurgersData:
    NAME_LEGTH = 8
    MAX_PRICE = 100
    INGREDIENT_TYPES = ['SAUCE', 'FILLING']
    RANDOM_NAME = Helper.random_name(NAME_LEGTH)
    RANDOM_PRICE = Helper.random_price(MAX_PRICE)
    RANDOM_INGREDIENT_TYPE = Helper.random_ingredient_type(INGREDIENT_TYPES)
