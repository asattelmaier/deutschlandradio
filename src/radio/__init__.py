from src.event_bus import EventBus
from .audio_player import AudioPlayer
from .g_object import GStreamer
from .radio import Play, Pause, Toggle, Next, Previous, UpdateMetaData, Channel, OnPlay, OnPause, OnMetaDataUpdate
from .radio import Radio


def create(event_bus: EventBus, current_channel: Channel) -> None:
    player = AudioPlayer.create(event_bus, GStreamer)

    Radio.create(player, event_bus, current_channel)
