from src.event_bus import Event


class Toggle(Event):
    name: str = 'toggle'
