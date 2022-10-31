from src.g_object import CheckMenuItem
from src.radio import Channel


class MenuItem:
    def __init__(self, item: CheckMenuItem, channel: Channel):
        self._item = item
        self._is_updating = False
        self._channel = channel

    @property
    def channel(self) -> Channel:
        return self._channel

    @property
    def is_active(self) -> bool:
        return self._item.get_active()

    @property
    def label(self) -> str:
        return self._item.get_label()

    @property
    def is_updating(self) -> bool:
        return self._is_updating

    def disable(self) -> None:
        self._item.set_active(False)

    def activate(self) -> None:
        self._is_updating = True
        self._item.set_active(True)

    def update_done(self):
        self._is_updating = False
