from __future__ import annotations

from src.event_bus import Subscription
from src.radio.events import Stop


class OnStop(Subscription):
    event_name: str = Stop.name
