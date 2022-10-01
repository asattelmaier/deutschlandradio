from src.event_bus import Event
from src.radio import Channel


class Play(Event):
    name: str = 'play'

    def __init__(self, channel: Channel):
        self.channel = channel
