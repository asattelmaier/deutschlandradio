from src.event_bus import Event
from ..radio import Channel


class Stop(Event):
    name: str = 'stop'

    def __init__(self, channel: Channel):
        self.channel = channel
