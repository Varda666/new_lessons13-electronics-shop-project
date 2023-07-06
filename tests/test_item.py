"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from electronics_shop.src import item
from electronics_shop.src import phone

@pytest.fixture
def item1():
    item1 = item.Item("Смартфон", 10000, 20)
    return item1

@pytest.fixture
def item2():
    item2 = item.Item("Компьютер", 40000, 2)
    return item2

@pytest.fixture
def item3():
    phone3 = phone.Phone("iPhone 14", 120_000, 5, 2)
    return phone3

@pytest.fixture
def item4():
    item4 = item.Item("Смартфон", 10000, 20)
    return item4



def test_calculate_total_price(item1):
    assert item.Item.calculate_total_price(item1) == 200000

def test_apply_discount(item2):
    item2.pay_rate = 0.75
    assert item.Item.apply_discount(item2) == 30000

def test_instantiate_from_csv():
    pass




def test_string_to_number():
    assert item.Item.string_to_number('24') == 24
    assert item.Item.string_to_number('28.2') == 28

    with pytest.raises(ValueError):
        item.Item.string_to_number('dfg.2')

def test__add__(item4, item3):
    assert item.Item.__add__(item4, item3) == 25
