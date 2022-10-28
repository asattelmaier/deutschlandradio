from typing import Callable
from src.event_bus import Subscription
from src.radio.events.toggle import Toggle


class OnToggle(Subscription):
    event_name: str = Toggle.name

    def __init__(self, handler: Callable[[Toggle], None]):
        super().__init__(handler)
