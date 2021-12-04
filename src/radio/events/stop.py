from __future__ import annotations

from src.event_bus import Event


class Stop(Event):
    name: str = 'stop'
