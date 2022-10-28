from .event import Event
from .subscription import Subscription


class EventBus:
    def __init__(self) -> None:
        self._subscriptions: [Subscription] = []

    def subscribe(self, subscription: Subscription) -> None:
        self._subscriptions.append(subscription)

    def publish(self, event: Event) -> None:
        for subscription in self._subscriptions:
            if subscription.event_name == event.name:
                subscription.notify(event)
