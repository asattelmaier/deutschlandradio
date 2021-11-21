import unittest
from unittest.mock import MagicMock, call

from ui import MenuBuilder


class TestMenuBuilder(unittest.TestCase):
    def test_creation(self):
        """
        Test that a MenuBuilder instance will be created.
        """
        gimp_toolkit = MagicMock()

        menu_builder = MenuBuilder.create(gimp_toolkit)

        self.assertIsInstance(menu_builder, MenuBuilder)

    def test_add_item(self):
        """
        Test that an item will be added to the menu.
        """
        gimp_toolkit = MagicMock()
        item = MagicMock()

        menu_builder = MenuBuilder.create(gimp_toolkit)
        gimp_toolkit.CheckMenuItem.return_value = item
        menu = menu_builder \
            .add_item('some-label', lambda: 'test') \
            .build()

        menu.append.assert_has_calls([call(item)])

    def test_add_multiple_items(self):
        """
        Test that multiple items will be added to the menu.
        """
        gimp_toolkit = MagicMock()
        item = MagicMock()

        menu_builder = MenuBuilder.create(gimp_toolkit)
        gimp_toolkit.CheckMenuItem.return_value = item
        menu = menu_builder \
            .add_item('some-label', lambda: 'test') \
            .add_item('some-label', lambda: 'test') \
            .build()

        menu.append.assert_has_calls([call(item), call(item)])

    def test_add_separator(self):
        """
        Test that a separator item will be added.
        """
        gimp_toolkit = MagicMock()
        item = MagicMock()
        separator = MagicMock()

        gimp_toolkit.CheckMenuItem.return_value = item
        gimp_toolkit.SeparatorMenuItem.return_value = separator
        menu_builder = MenuBuilder.create(gimp_toolkit)
        menu = menu_builder \
            .add_item('some-label', lambda: 'test') \
            .add_separator() \
            .add_item('some-label', lambda: 'test') \
            .build()

        menu.append.assert_has_calls([call(item), call(separator), call(item)])
