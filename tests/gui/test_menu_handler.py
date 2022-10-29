import unittest
from unittest.mock import MagicMock
from src.gui import MenuHandler
from src.radio import Pause, Play
from tests.mocks.event_bus_mock import EventBusMock


class TestMenuHandler(unittest.TestCase):
    def test_plays_disabled_item(self):
        """
        Test that the disabled item gets played.
        """
        item = MagicMock()
        event_bus = EventBusMock()
        quit_handler = MagicMock()
        menu_handler = MenuHandler.create(event_bus, quit_handler)

        item.get_label.return_value = 'Deutschlandfunk'
        item.get_active.return_value = True
        menu_handler.add_item(item)
        menu_handler.item_handler(item)
        event = event_bus.get_event(Play)

        self.assertIsInstance(event, Play)

    def test_stops_active_item(self):
        """
        Test that the active item gets stopped.
        """
        item = MagicMock()
        event_bus = EventBusMock()
        quit_handler = MagicMock()
        menu_handler = MenuHandler.create(event_bus, quit_handler)

        item.get_label.return_value = 'Deutschlandfunk'
        item.get_active.return_value = False
        menu_handler.add_item(item)
        menu_handler.item_handler(item)
        event = event_bus.get_event(Pause)

        print(event_bus._events)
        self.assertIsInstance(event, Pause)
