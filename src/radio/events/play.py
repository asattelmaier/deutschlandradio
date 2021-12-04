from __future__ import annotations

from src.event_bus import Event


class Play(Event):
    name: str = 'play'
