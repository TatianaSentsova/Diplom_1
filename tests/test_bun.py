from praktikum.bun import Bun


class TestBun:
    def test_name_of_bun_true(self):
        bun = Bun('Пояс астероидов', 123)
        assert bun.name == 'Пояс астероидов'

    def test_price_of_bun_true(self):
        bun = Bun('Пояс астероидов', 123)
        assert bun.price == 123

    def test_get_name_of_bun(self):
        bun = Bun('Пояс астероидов', 123)
        assert bun.get_name() == 'Пояс астероидов'

    def test_get_price_of_bun(self):
        bun = Bun('Пояс астероидов', 123)
        assert bun.get_price() == 123
