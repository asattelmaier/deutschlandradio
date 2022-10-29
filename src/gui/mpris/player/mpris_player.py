from gi.repository.GLib import Variant
from pydbus.generic import signal

from src.event_bus import EventBus
from src.radio import OnPlay, OnPause, Play, Pause, Channel, Toggle, Next, Previous
from .playback_status import PlaybackStatus
from .title_map import TitleMap


class MprisPlayer:
    """
    API Documentation:
    https://specifications.freedesktop.org/mpris-spec/2.2/Player_Interface.html
    """

    dbus = """
    <node>
      <interface name="org.mpris.MediaPlayer2.Player">
        <property name="CanPlay" type="b" access="read"/>
        <property name="CanPause" type="b" access="read"/>
        <property name="CanGoNext" type="b" access="read"/>
        <property name="CanGoPrevious" type="b" access="read"/>
        <property name="PlaybackStatus" type="s" access="read"/>
        <property name="Metadata" type="a{sv}" access="read"/>
        <method name="Next"/>
        <method name="Previous"/>
        <method name="Pause"/>
        <method name="PlayPause"/>
        <method name="Stop"/>
        <method name="Play"/>
      </interface>
    </node>
    """
    CanPlay = True
    CanPause = True
    CanGoNext = True
    CanGoPrevious = True
    PlaybackStatus = PlaybackStatus.STOPPED.value
    PropertiesChanged = signal()
    Metadata = {'xesam:title': Variant('s', 'Rundfunk'), 'xesam:artist': Variant('as', [' '])}

    def __init__(self, main_interface: str, event_bus: EventBus) -> None:
        self._interface: str = f'{main_interface}.Player'
        self._event_bus = event_bus

        event_bus.subscribe(OnPlay(self._on_play))
        event_bus.subscribe(OnPause(self._on_pause))

    def Next(self):
        self._event_bus.publish(Next())

    def Previous(self):
        self._event_bus.publish(Previous())

    def PlayPause(self) -> None:
        self._event_bus.publish(Toggle())

    def _on_play(self, event: Play) -> None:
        self._update_playback_status(PlaybackStatus.PLAYING)
        self._update_meta_data(event.channel)

    def _on_pause(self, event: Pause) -> None:
        self._update_playback_status(PlaybackStatus.PAUSED)
        self._update_meta_data(event.channel)

    def _update_playback_status(self, playback_status: PlaybackStatus) -> None:
        self._update({'PlaybackStatus': playback_status.value})

    def _update_meta_data(self, channel: Channel) -> None:
        title = Variant('s', TitleMap.get_label(channel))
        artist = Variant('as', [' '])

        self._update({'Metadata': {'xesam:title': title, 'xesam:artist': artist}})

    def _update(self, properties: dict) -> None:
        self.PropertiesChanged(self._interface, properties, [])
