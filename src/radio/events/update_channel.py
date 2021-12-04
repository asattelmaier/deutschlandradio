from __future__ import annotations

from src.event_bus import Event
from src.radio import Channel


class UpdateChannel(Event):
    name: str = 'update-channel'

    def __init__(self, channel: Channel):
        self.channel = channel
