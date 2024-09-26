import pytest

from praktikum.bun import Bun


@pytest.fixture()
def bun(n, a):
    return Bun(n, a)