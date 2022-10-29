from src.event_bus import Event
from ..radio import Channel


class Pause(Event):
    name: str = 'pause'

    def __init__(self, channel: Channel):
        self.channel = channel
