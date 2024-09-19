from praktikum.ingredient import Ingredient


class TestBurger:

    def test_ingredient_type_true(self):
        ingredient = Ingredient('Соус', 'Космическое чили', 14)
        assert ingredient.type == 'Соус'

    def test_name_og_ingredient_true(self):
        ingredient = Ingredient('Соус', 'Космическое чили', 14)
        assert ingredient.name == 'Космическое чили'

    def test_price_of_ingredient_true(self):
        ingredient = Ingredient('Соус', 'Космическое чили', 14)
        assert ingredient.price == 14

    def test_get_price_ingredient(self):
        ingredient = Ingredient('Соус', 'Космическое чили', 14)
        assert ingredient.get_price() == 14

    def test_get_name_ingredient(self):
        ingredient = Ingredient('Соус', 'Космическое чили', 14)
        assert ingredient.get_name() == 'Космическое чили'

    def test_get_type(self):
        ingredient = Ingredient('Соус', 'Космическое чили', 14)
        assert ingredient.get_type() == 'Соус'
