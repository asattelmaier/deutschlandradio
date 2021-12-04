from __future__ import annotations

from src.event_bus import Subscription
from src.radio.events import ChangeChannel


class OnChannelChange(Subscription):
    event_name: str = ChangeChannel.name
