from __future__ import annotations
from src.radio import AudioPlayer, Channel


class Radio:
    def __init__(self, audio_player: AudioPlayer, current_channel: Channel):
        self._audio_player = audio_player
        self._current_channel = current_channel

    @staticmethod
    def create(audio_player: AudioPlayer, current_channel: Channel) -> Radio:
        audio_player.set_uri(current_channel.value)

        return Radio(audio_player, current_channel)

    @property
    def is_playing(self) -> bool:
        return self._audio_player.is_playing

    def update_channel(self, channel: Channel) -> None:
        is_current_channel = channel is self._current_channel

        if is_current_channel:
            return self._toggle_audio_player()

        self._change_channel(channel)

    def _toggle_audio_player(self) -> None:
        if self._audio_player.is_playing:
            return self._audio_player.stop()

        self._audio_player.play()

    def _change_channel(self, channel: Channel) -> None:
        self._current_channel = channel
        self._audio_player.stop()
        self._audio_player.set_uri(channel.value)
        self._audio_player.play()
