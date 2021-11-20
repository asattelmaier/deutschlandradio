import unittest
from unittest.mock import MagicMock, call

from ui import MenuBuilder


class TestMenuBuilder(unittest.TestCase):
    def test_creation(self):
        """
        Test that a MenuBuilder instance will be created.
        """
        menu_factory = MagicMock()
        item_factory = MagicMock()

        menu_builder = MenuBuilder.create(menu_factory, item_factory)

        self.assertIsInstance(menu_builder, MenuBuilder)

    def test_add_item(self):
        """
        Test that an item will be added to the menu.
        """
        menu_factory = MagicMock()
        item_factory = MagicMock()
        item = MagicMock()

        menu_builder = MenuBuilder.create(menu_factory, item_factory)
        item_factory.return_value = item
        menu = menu_builder \
            .add_item('some-label', lambda: 'test') \
            .build()

        menu.append.assert_has_calls([call(item)])

    def test_add_multiple_items(self):
        """
        Test that multiple items will be added to the menu.
        """
        menu_factory = MagicMock()
        item_factory = MagicMock()
        item = MagicMock()

        menu_builder = MenuBuilder.create(menu_factory, item_factory)
        item_factory.return_value = item
        menu = menu_builder \
            .add_item('some-label', lambda: 'test') \
            .add_item('some-label', lambda: 'test') \
            .build()

        menu.append.assert_has_calls([call(item), call(item)])
