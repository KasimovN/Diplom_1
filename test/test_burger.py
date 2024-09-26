import pytest

from praktikum.burger import Burger


class TestBurger:
    @pytest.mark.parametrize('atribute, value', [['bun', None], ['ingredients', []]])
    def test_default_atributes(self, atribute, value):
        burger = Burger()
        assert getattr(burger, atribute) == value

    def test_set_buns(self, mock_bun):
        bun = mock_bun
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, mock_ingredient1):
        ingr1 = mock_ingredient1
        burger = Burger()
        burger.add_ingredient(ingr1)
        assert burger.ingredients == [ingr1]

    def test_remove_ingredient(self, mock_ingredient1):
        ingr1 = mock_ingredient1
        burger = Burger()
        burger.add_ingredient(ingr1)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, mock_ingredient1, mock_ingredient2):
        ingr1 = mock_ingredient1
        ingr2 = mock_ingredient2
        burger = Burger()
        burger.add_ingredient(ingr1)
        burger.add_ingredient(ingr2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingr2, ingr1]

    def test_get_price(self, mock_bun, mock_ingredient1):
        ingr1 = mock_ingredient1
        bun = mock_bun
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingr1)
        assert burger.get_price() == bun.get_price() * 2 + mock_ingredient1.get_price()

    def test_get_receipt(self, mock_bun, mock_ingredient1):
        ingr1 = mock_ingredient1
        bun = mock_bun
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingr1)
        receipt = [f'(==== {bun.get_name()} ====)', f'= {str(ingr1.get_type()).lower()} {ingr1.get_name()} =',
                   f'(==== {bun.get_name()} ====)\n', f'Price: {burger.get_price()}']
        assert burger.get_receipt() == '\n'.join(receipt)
