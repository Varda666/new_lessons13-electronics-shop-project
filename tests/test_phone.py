import pytest
from electronics_shop.src import item
from electronics_shop.src import phone

@pytest.fixture
def item3():
    phone3 = phone.Phone("iPhone 14", 120_000, 5, 2)
    return phone3

@pytest.fixture
def item4():
    phone4 = phone.Phone("iPhone 123", 2_000_000, 1, 25)
    return phone4

def test__init__(item3):
    assert item3.sim_quantity == 2

def test__repr__(item3):
    assert phone.Phone.__repr__(item3) == "Phone('iPhone 14', 120000, 5, 2)"

def test__add__(item3, item4):
    assert phone.Phone.__add__(item3, item4) == 6