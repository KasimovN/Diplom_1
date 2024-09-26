import pytest

from data import StarBurgersData
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('atribute, value', [['name', StarBurgersData.RANDOM_NAME],
                                                 ['price', StarBurgersData.RANDOM_PRICE]])
    def test_bun_atribute(self, atribute, value):
        bun = Bun(StarBurgersData.RANDOM_NAME, StarBurgersData.RANDOM_PRICE)
        assert getattr(bun, atribute) == value

    def test_get_name(self):
        bun = Bun(StarBurgersData.RANDOM_NAME, StarBurgersData.RANDOM_PRICE)
        assert bun.get_name() == StarBurgersData.RANDOM_NAME

    def test_get_price(self):
        bun = Bun(StarBurgersData.RANDOM_NAME, StarBurgersData.RANDOM_PRICE)
        assert bun.get_price() == StarBurgersData.RANDOM_PRICE
