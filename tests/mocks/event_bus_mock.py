from typing import Any
from unittest.mock import MagicMock


class EventBusMock(MagicMock):
    def __init__(self, *args: Any, **kw: Any):
        super().__init__(*args, **kw)
        self._subscriptions = []
        self._events = []
        self._subscription = None

    @property
    def events(self):
        return self._events

    def subscribe(self, subscription):
        self._subscriptions.append(subscription)

    def publish(self, event):
        self._events.append(event)

    def get_subscription(self, subscription):
        found_subscriptions = filter(
            lambda current_subscription: subscription.event_name == current_subscription.event_name, self._subscriptions
        )

        for found_subscription in found_subscriptions:
            self._subscription = found_subscription

            return self

    def notify(self, event):
        self._subscription.notify(event)

        return self

    def get_event(self, event):
        found_events = filter(lambda current_event: event.name == current_event.name, self._events)

        for found_event in found_events:
            return found_event
