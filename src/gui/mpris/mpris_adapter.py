from __future__ import annotations
from src.event_bus import EventBus
from src.radio import Stop, Play, Channel, OnPlay, OnStop
from .mpris_server import MprisAdapterInterface, PlayState, Metadata, MetadataObj, EventAdapter
from ..menu_item import MenuItemLabelChannelMap


class MprisAdapter(MprisAdapterInterface):
    _TITLE: str = 'Aktueller Sender:'
    _event_adapter: EventAdapter

    def __init__(self, event_bus: EventBus, current_channel: Channel):
        self._event_bus: EventBus = event_bus
        self._is_playing: bool = False
        self._current_channel: Channel = current_channel

    @staticmethod
    def create(event_bus: EventBus, current_channel: Channel) -> MprisAdapter:
        mpris_adapter = MprisAdapter(event_bus, current_channel)

        event_bus.subscribe(OnPlay(mpris_adapter._on_play))
        event_bus.subscribe(OnStop(mpris_adapter._on_stop))

        return mpris_adapter

    def set_event_adapter(self, event_adapter: EventAdapter) -> None:
        self._event_adapter = event_adapter

    def _on_play(self, event: Play) -> None:
        self._update_state(is_playing=True, channel=event.channel)

    def _on_stop(self, event: Stop) -> None:
        self._update_state(is_playing=False, channel=event.channel)

    def can_play(self) -> bool:
        return True

    def can_pause(self) -> bool:
        return True

    def get_current_position(self):
        return 0

    def pause(self):
        self._event_bus.publish(Stop(self._current_channel))

    def play(self):
        self._event_bus.publish(Play(self._current_channel))

    def get_playstate(self):
        if self._is_playing:
            return PlayState.PLAYING

        return PlayState.STOPPED

    def metadata(self) -> Metadata:
        label = MenuItemLabelChannelMap.get_label(self._current_channel)

        return MetadataObj(
            url=[self._TITLE],
            length=label,
        )

    def _update_state(self, is_playing: bool, channel: Channel):
        self._is_playing = is_playing
        self._current_channel = channel
        self._event_adapter.on_player_all()
