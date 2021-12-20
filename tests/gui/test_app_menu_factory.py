import unittest
from unittest.mock import MagicMock, call
from src.gui import AppMenuFactory


class TestAppMenuFactory(unittest.TestCase):
    def test_creation(self):
        """
        Test that the Menu will be created.
        """
        menu_builder = MagicMock()
        radio = MagicMock()
        channel = MagicMock()
        menu = MagicMock()

        menu_builder.add_item.return_value = menu_builder
        menu_builder.add_separator.return_value = menu_builder
        menu_builder.build.return_value = menu
        app_menu_factory = AppMenuFactory(menu_builder, radio, channel)

        self.assertIs(app_menu_factory.create(), menu)

    def test_menu_label_order(self):
        """
        Test the order of the menu items.
        """

        menu_builder = MagicMock()
        radio = MagicMock()
        channel = MagicMock()

        menu_builder.add_item.return_value = menu_builder
        menu_builder.add_separator.return_value = menu_builder
        app_menu_factory = AppMenuFactory(menu_builder, radio, channel)
        app_menu_factory.create()

        menu_builder.add_item.assert_has_calls([
            call('Deutschlandfunk'),
            call('Deutschlandfunk Kultur'),
            call('Deutschlandfunk Nova'),
            call('Dokumente und Debatten'),
            call('Schließen')
        ])
