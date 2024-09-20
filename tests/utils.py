from unittest.mock import Mock


class Utils:
    @staticmethod
    def mock_bun(bun):
        mock = Mock()
        mock.get_name.return_value = bun[0]
        mock.get_price.return_value = bun[1]
        return mock

    @staticmethod
    def mock_ingredient(ingredient):
        mock = Mock()
        mock.get_type.return_value = ingredient[0]
        mock.get_name.return_value = ingredient[1]
        mock.get_price.return_value = ingredient[2]
        return mock
