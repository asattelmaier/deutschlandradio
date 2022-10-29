from typing import Callable
from src.event_bus import Subscription
from src.radio.events import Pause


class OnPause(Subscription):
    event_name: str = Pause.name

    def __init__(self, handler: Callable[[Pause], None]):
        super().__init__(handler)
