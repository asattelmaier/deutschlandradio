import unittest
from unittest.mock import MagicMock
from src.event_bus import EventBus


class TestEventBus(unittest.TestCase):
    def test_subscription_notification(self):
        """
        Test that only subscriptions with same events gets notified.
        """
        event_bus = EventBus()
        first_subscription = MagicMock()
        second_subscription = MagicMock()
        third_subscription = MagicMock()
        event = MagicMock()

        first_subscription.event_name = 'Some Event'
        second_subscription.event_name = 'Some Other Event'
        third_subscription.event_name = 'Some Event'
        event.name = 'Some Event'
        event_bus.subscribe(first_subscription)
        event_bus.subscribe(second_subscription)
        event_bus.subscribe(third_subscription)
        event_bus.publish(event)

        first_subscription.notify.assert_called_once_with(event)
        second_subscription.notify.assert_not_called()
        third_subscription.notify.assert_called_once_with(event)
