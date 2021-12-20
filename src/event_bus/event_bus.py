from __future__ import annotations
from .event import Event
from .subscription import Subscription


class EventBus:
    def __init__(self):
        self._subscriptions: [Subscription] = []

    def subscribe(self, subscription: Subscription):
        self._subscriptions.append(subscription)

    def publish(self, event: Event):
        for subscription in self._subscriptions:
            if subscription.event_name == event.name:
                subscription.notify(event)
