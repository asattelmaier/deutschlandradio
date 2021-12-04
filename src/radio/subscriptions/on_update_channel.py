from __future__ import annotations

from src.event_bus import Subscription
from src.radio.events import UpdateChannel


class OnUpdateChannel(Subscription):
    event_name: str = UpdateChannel.name
