import pytest

from data import StarBurgersData
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize('atribute, value', [['name', StarBurgersData.RANDOM_NAME],
                                                 ['price', StarBurgersData.RANDOM_PRICE],
                                                 ['type', StarBurgersData.RANDOM_INGREDIENT_TYPE]])
    def test_ingredients_atribute(self, atribute, value):
        ing = Ingredient(StarBurgersData.RANDOM_INGREDIENT_TYPE, StarBurgersData.RANDOM_NAME,
                         StarBurgersData.RANDOM_PRICE)
        assert getattr(ing, atribute) == value

    def test_get_name(self):
        ing = Ingredient(StarBurgersData.RANDOM_INGREDIENT_TYPE, StarBurgersData.RANDOM_NAME,
                         StarBurgersData.RANDOM_PRICE)
        assert ing.get_name() == StarBurgersData.RANDOM_NAME

    def test_get_price(self):
        ing = Ingredient(StarBurgersData.RANDOM_INGREDIENT_TYPE, StarBurgersData.RANDOM_NAME,
                         StarBurgersData.RANDOM_PRICE)
        assert ing.get_price() == StarBurgersData.RANDOM_PRICE

    def test_get_type(self):
        ing = Ingredient(StarBurgersData.RANDOM_INGREDIENT_TYPE, StarBurgersData.RANDOM_NAME,
                         StarBurgersData.RANDOM_PRICE)
        assert ing.get_type() == StarBurgersData.RANDOM_INGREDIENT_TYPE
