from typing import Callable

from src.event_bus import Subscription
from src.radio.events import Next


class OnNext(Subscription):
    event_name: str = Next.name

    def __init__(self, handler: Callable[[Next], None]):
        super().__init__(handler)
