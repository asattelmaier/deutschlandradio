from __future__ import annotations
from typing import Callable
from src.g_object import CheckMenuItem
from src.radio import Channel


class MenuItem:
    def __init__(self, item: CheckMenuItem, channel: Channel, handler: Callable):
        self._item = item
        self._channel = channel
        self._handler = handler

    @property
    def is_active(self) -> bool:
        return self._item.get_active()

    @property
    def label(self) -> str:
        return self._item.get_label()

    def disable(self) -> None:
        self._item.set_active(False)
