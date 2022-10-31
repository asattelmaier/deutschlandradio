from src.event_bus import Event
from src.radio.radio import Channel


class Pause(Event):
    name: str = 'radio::pause'

    def __init__(self, channel: Channel):
        self.channel = channel
