from __future__ import annotations

from src.event_bus import EventBus
from .channel import Channel
from .audio_player import AudioPlayer
from .events import Stop, Play, ChangeChannel, UpdateChannel
from .subscriptions import OnPlay, OnStop, OnChannelChange, OnUpdateChannel


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
        event_bus.subscribe(OnChannelChange(radio._on_change_channel))
        event_bus.subscribe(OnUpdateChannel(radio._on_update_channel))

    @property
    def is_playing(self) -> bool:
        return self._audio_player.is_playing

    def _on_update_channel(self, event: UpdateChannel) -> None:
        is_current_channel = event.channel is self._current_channel

        if is_current_channel:
            return self._toggle_audio_player()

        self._change_channel(event.channel)

    def _on_play(self, _: Play):
        self._audio_player.play()

    def _on_stop(self, _: Stop):
        self._audio_player.stop()

    def _on_change_channel(self, event: ChangeChannel):
        self._set_channel(event.channel)

    def _set_channel(self, channel: Channel) -> None:
        self._current_channel = channel
        self._audio_player.set_uri(channel.value)

    def _toggle_audio_player(self) -> None:
        if self.is_playing:
            return self._event_bus.publish(Stop())

        self._event_bus.publish(Play())

    def _change_channel(self, channel: Channel) -> None:
        self._event_bus.publish(Stop())
        self._event_bus.publish(ChangeChannel(channel))
        self._event_bus.publish(Play())
