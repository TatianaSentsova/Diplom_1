from praktikum.burger import Burger
import pytest

class TestBurger:

    @pytest.mark.parametrize('ingredient_type, name, price', ['Соус', 'Космическое чили', 14])
    def test_ingredient_init(self, ingredient_type, name, price):
        ingredient =
