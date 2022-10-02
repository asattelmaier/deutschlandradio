from g_object import GStreamer, GimpToolkit, AppIndicator
from event_bus import EventBus
from gui import AppMenuFactory, MenuBuilder, MenuHandler, MprisMediaPlayer
from radio import Radio, Channel, AudioPlayer
from app import NAME, ICON, CATEGORY


def main() -> None:
    current_channel = Channel.DEUTSCHLANDFUNK
    event_bus = EventBus()
    audio_player = AudioPlayer.create(GStreamer)
    radio = Radio.create(audio_player, event_bus, current_channel)
    menu_handler = MenuHandler.create(event_bus, GimpToolkit.main_quit)
    menu_builder = MenuBuilder.create(GimpToolkit, menu_handler)
    app_menu_factory = AppMenuFactory(menu_builder, event_bus, Channel)
    indicator = AppIndicator.Indicator.new(NAME, ICON, CATEGORY)
    mpris_media_player = MprisMediaPlayer(NAME, radio, event_bus)

    mpris_media_player.publish()
    indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(app_menu_factory.create())

    GimpToolkit.main()


if __name__ == "__main__":
    main()
