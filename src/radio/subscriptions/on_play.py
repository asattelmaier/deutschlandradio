from __future__ import annotations

from src.event_bus import Subscription
from src.radio.events import Play


class OnPlay(Subscription):
    event_name: str = Play.name
