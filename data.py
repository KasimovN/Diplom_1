from helper import Helper


class StarBurgersData:
    NAME_LEGTH = 4
    MAX_PRICE = 100
    INGREDIENT_TYPES = ['SAUCE', 'FILLING']
    RANDOM_NAME = Helper.random_name(NAME_LEGTH)
    RANDOM_PRICE = Helper.random_price(MAX_PRICE)
    RANDOM_INGREDIENT_TYPE = Helper.random_ingredient_type(INGREDIENT_TYPES)
    DATABASE_BUN_NAME_LIST = ["black bun", "white bun", "red bun"]
    DATABASE_BUN_SUM_PRICE = 100*1 + 200*2 + 300*3
    DATABASE_INGREDIENT_NAME_LIST = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
    DATABASE_INGREDIENT_SUM_PRICE = 100*1 + 200*2 + 300*3 + 100*4 + 200*5 + 300*6
