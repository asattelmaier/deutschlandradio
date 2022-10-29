from src.event_bus import EventBus
from .g_object import GStreamer
from .audio_player import AudioPlayer
from .channel import Channel
from .radio import Radio


def create(event_bus: EventBus, current_channel: Channel) -> None:
    audio_player = AudioPlayer.create(GStreamer)

    Radio.create(audio_player, event_bus, current_channel)
