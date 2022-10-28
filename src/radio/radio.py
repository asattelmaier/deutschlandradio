from src.event_bus import EventBus
from .audio_player import AudioPlayer
from .channel import Channel
from .channel_order_map import ChannelOrderMap
from .events import Stop, Play, Toggle, Next, Previous
from .subscriptions import OnPlay, OnStop, OnToggle, OnNext, OnPrevious


class Radio:
    _current_channel: Channel

    def __init__(self, audio_player: AudioPlayer, event_bus: EventBus):
        self._audio_player = audio_player
        self._event_bus = event_bus

    @staticmethod
    def create(audio_player: AudioPlayer, event_bus: EventBus, current_channel: Channel):
        radio = Radio(audio_player, event_bus)

        radio._set_channel(current_channel)
        event_bus.subscribe(OnPlay(radio._on_play))
        event_bus.subscribe(OnStop(radio._on_stop))
        event_bus.subscribe(OnToggle(radio._on_toggle))
        event_bus.subscribe(OnNext(radio._on_next))
        event_bus.subscribe(OnPrevious(radio._on_previous))

        return radio

    def _on_next(self, _: Next) -> None:
        self._play(ChannelOrderMap.next(self._current_channel))

    def _on_previous(self, _: Previous) -> None:
        self._play(ChannelOrderMap.previous(self._current_channel))

    def _on_toggle(self, _: Toggle) -> None:
        if self._audio_player.is_playing:
            return self._stop(self._current_channel)

        self._play(self._current_channel)

    def _on_play(self, event: Play) -> None:
        if event.channel.value == self._current_channel.value:
            return self._audio_player.play()

        self._change_channel(event.channel)

    def _on_stop(self, event: Stop) -> None:
        if event.channel.value == self._current_channel.value:
            self._audio_player.stop()

    def _play(self, channel: Channel) -> None:
        self._event_bus.publish(Play(channel))

    def _stop(self, channel: Channel) -> None:
        self._event_bus.publish(Stop(channel))

    def _set_channel(self, channel: Channel) -> None:
        self._current_channel = channel
        self._audio_player.set_uri(channel.value)

    def _change_channel(self, channel: Channel) -> None:
        self._audio_player.stop()
        self._set_channel(channel)
        self._audio_player.play()
