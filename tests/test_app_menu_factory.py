import unittest
from unittest.mock import MagicMock, call, ANY

from ui import AppMenuFactory


class TestAppMenuFactory(unittest.TestCase):
    def test_creation(self):
        """
        Test that the Menu will be created.
        """
        menu_builder = MagicMock()
        radio = MagicMock()
        channel = MagicMock()
        quit_handler = MagicMock()
        menu = MagicMock()

        app_menu_factory = AppMenuFactory(menu_builder, radio, channel, quit_handler)
        menu_builder.add_item.return_value = menu_builder
        menu_builder.build.return_value = menu

        self.assertIs(app_menu_factory.create(), menu)

    def test_menu_label_order(self):
        """
        Test the order of the menu items.
        """

        menu_builder = MagicMock()
        radio = MagicMock()
        channel = MagicMock()
        quit_handler = MagicMock()

        menu_builder.add_item.return_value = menu_builder
        app_menu_factory = AppMenuFactory(menu_builder, radio, channel, quit_handler)
        app_menu_factory.create()

        menu_builder.add_item.assert_has_calls([
            call('Deutschlandfunk', ANY),
            call('Deutschlandfunk Kultur', ANY),
            call('Deutschlandfunk Nova', ANY),
            call('Dokumente und Debatten', ANY),
            call('Schließen', ANY)
        ])
