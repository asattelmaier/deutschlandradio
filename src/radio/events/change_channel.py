from __future__ import annotations

from src.event_bus import Event
from src.radio import Channel


class ChangeChannel(Event):
    name: str = 'change-channel'

    def __init__(self, channel: Channel):
        self.channel = channel
