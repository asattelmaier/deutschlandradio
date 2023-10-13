from src.event_bus import Event
from src.radio.radio import Channel


class Play(Event):
    name: str = 'radio::play'

    def __init__(self, channel: Channel):
        self.channel = channel
