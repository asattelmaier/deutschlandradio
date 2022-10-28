from typing import Callable
from src.event_bus import Subscription
from src.radio.events import Stop


class OnStop(Subscription):
    event_name: str = Stop.name

    def __init__(self, handler: Callable[[Stop], None]):
        super().__init__(handler)
