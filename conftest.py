from unittest.mock import Mock

import pytest

from data import StarBurgersData


@pytest.fixture()
def mock_ingredient1():
    ingredient = Mock()
    ingredient.get_name.return_value = f'Mock_ing1_{StarBurgersData.RANDOM_NAME}'
    ingredient.get_price.return_value = StarBurgersData.RANDOM_PRICE
    ingredient.get_type.return_value = StarBurgersData.RANDOM_INGREDIENT_TYPE
    return ingredient
@pytest.fixture()
def mock_ingredient2():
    ingredient = Mock()
    ingredient.get_name.return_value = f'Mock_ing2_{StarBurgersData.RANDOM_NAME}'
    ingredient.get_price.return_value = StarBurgersData.RANDOM_PRICE + 1
    ingredient.get_type.return_value = StarBurgersData.RANDOM_INGREDIENT_TYPE
    return ingredient

@pytest.fixture()
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = f'Mock_bun_{StarBurgersData.RANDOM_NAME}'
    bun.get_price.return_value = StarBurgersData.RANDOM_PRICE * 2
    return bun
