from __future__ import annotations
from typing import Type
from src.g_object import GStreamer, State
from .playbin import Playbin


class AudioPlayer:
    def __init__(self, player: Playbin, player_state: State):
        self._player = player
        self._player_state = player_state

    @staticmethod
    def create(g_streamer: Type[GStreamer]) -> AudioPlayer:
        g_streamer.init(None)
        player = g_streamer.ElementFactory.make("playbin", "player")

        return AudioPlayer(player, g_streamer.State)

    @property
    def is_playing(self) -> bool:
        current_state = self._player.current_state

        return current_state is self._player_state.PLAYING or current_state is self._player_state.READY

    def set_uri(self, uri) -> None:
        self._player.set_property('uri', uri)

    def play(self) -> None:
        self._player.set_state(self._player_state.PLAYING)

    def stop(self) -> None:
        self._player.set_state(self._player_state.NULL)
