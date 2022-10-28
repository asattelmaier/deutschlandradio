from app import NAME, ICON, CATEGORY
from event_bus import EventBus
from g_object import GStreamer, GimpToolkit, AppIndicator
from gui import AppMenuFactory, MenuBuilder, MenuHandler, MprisMediaPlayer
from radio import Radio, Channel, AudioPlayer


def main() -> None:
    current_channel = Channel.DEUTSCHLANDFUNK
    event_bus = EventBus()
    audio_player = AudioPlayer.create(GStreamer)
    menu_handler = MenuHandler.create(event_bus, GimpToolkit.main_quit)
    menu_builder = MenuBuilder.create(GimpToolkit, menu_handler)
    app_menu_factory = AppMenuFactory(menu_builder, Channel)
    indicator = AppIndicator.Indicator.new(NAME, ICON, CATEGORY)
    mpris_media_player = MprisMediaPlayer(NAME, event_bus)

    Radio.create(audio_player, event_bus, current_channel)
    mpris_media_player.publish()
    indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(app_menu_factory.create())

    GimpToolkit.main()


if __name__ == "__main__":
    main()
