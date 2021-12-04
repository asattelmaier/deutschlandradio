from __future__ import annotations

from typing import Callable

from .event import Event


class Subscription:
    event_name: str = ''

    def __init__(self, handler: Callable):
        self._handler = handler

    def notify(self, event: Event):
        self._handler(event)
