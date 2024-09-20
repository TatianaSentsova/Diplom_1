import allure
from praktikum.bun import Bun
from tests.data_test import BunConstants as BC


class TestBun:
    @allure.title('Проверка корректности имени в созданном экземпляре класса булка')
    def test_name_of_bun_true(self):
        bun = Bun(BC.BUN_NAME, BC.BUN_PRICE)
        assert bun.name == BC.BUN_NAME

    @allure.title('Проверка корректности цены в созданной экземпляре класса булка')
    def test_price_of_bun_true(self):
        bun = Bun(BC.BUN_NAME, BC.BUN_PRICE)
        assert bun.price == BC.BUN_PRICE

    @allure.title('Успешное получение названия булки')
    def test_get_name_of_bun(self):
        bun = Bun(BC.BUN_NAME, BC.BUN_PRICE)
        assert bun.get_name() == BC.BUN_NAME

    @allure.title('Успешное получение цены булки')
    def test_get_price_of_bun(self):
        bun = Bun(BC.BUN_NAME, BC.BUN_PRICE)
        assert bun.get_price() == BC.BUN_PRICE
