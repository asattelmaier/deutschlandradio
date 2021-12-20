from __future__ import annotations
from src.event_bus import EventBus
from .channel import Channel
from .audio_player import AudioPlayer
from .events import Stop, Play
from .subscriptions import OnPlay, OnStop


class Radio:
    _current_channel: Channel

    def __init__(self, audio_player: AudioPlayer, event_bus: EventBus):
        self._audio_player = audio_player
        self._event_bus = event_bus

    @staticmethod
    def init(audio_player: AudioPlayer, event_bus: EventBus, current_channel: Channel) -> None:
        radio = Radio(audio_player, event_bus)

        radio._set_channel(current_channel)

        event_bus.subscribe(OnPlay(radio._on_play))
        event_bus.subscribe(OnStop(radio._on_stop))

    def _on_play(self, event: Play) -> None:
        if event.channel.value == self._current_channel.value:
            return self._audio_player.play()

        self._change_channel(event.channel)

    def _on_stop(self, event: Stop):
        if event.channel.value == self._current_channel.value:
            self._audio_player.stop()

    def _set_channel(self, channel: Channel) -> None:
        self._current_channel = channel
        self._audio_player.set_uri(channel.value)

    def _change_channel(self, channel: Channel) -> None:
        self._audio_player.stop()
        self._set_channel(channel)
        self._audio_player.play()
