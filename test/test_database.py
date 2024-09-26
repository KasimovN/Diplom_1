from data import StarBurgersData
from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        database = Database()
        name_list = []
        sum_bun = 0
        for i in range(3):
            name_list.append(database.available_buns()[i].get_name())
            sum_bun += database.available_buns()[i].get_price() * (i+1)
        assert name_list == StarBurgersData.DATABASE_BUN_NAME_LIST and sum_bun == StarBurgersData.DATABASE_BUN_SUM_PRICE

    def test_available_ingredients(self):
        database = Database()
        name_list = []
        sum_bun = 0
        for i in range(6):
            name_list.append(database.available_ingredients()[i].get_name())
            sum_bun += database.available_ingredients()[i].get_price() * (i+1)
        assert (name_list == StarBurgersData.DATABASE_INGREDIENT_NAME_LIST
                and sum_bun == StarBurgersData.DATABASE_INGREDIENT_SUM_PRICE)
