"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from electronics_shop.src import item

@pytest.fixture
def item1():
    item1 = item.Item("Смартфон", 10000, 20)
    return item1

@pytest.fixture
def item2():
    item2 = item.Item("Компьютер", 40000, 2)
    return item2

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