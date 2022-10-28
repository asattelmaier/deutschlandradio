import unittest
from unittest.mock import MagicMock
from src.event_bus import Subscription


class TestSubscription(unittest.TestCase):
    def test_subscription_notification(self):
        """
        Test that the subscription handler gets called on notification.
        """
        handler = MagicMock()
        subscription = Subscription(handler)
        event = MagicMock()

        subscription.notify(event)

        handler.assert_called_once_with(event)
