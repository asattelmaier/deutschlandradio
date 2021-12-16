from __future__ import annotations
from g_object import GStreamer, GimpToolkit, AppIndicator
from event_bus import EventBus
from gui import AppMenuFactory, MenuBuilder, MenuHandler
from radio import Radio, Channel, AudioPlayer


def main() -> None:
    event_bus = EventBus()
    audio_player = AudioPlayer.create(GStreamer)
    Radio.init(audio_player, event_bus, Channel.DEUTSCHLANDFUNK)
    menu_handler = MenuHandler(event_bus)
    menu_builder = MenuBuilder.create(GimpToolkit, menu_handler)
    app_menu_factory = AppMenuFactory(menu_builder, event_bus, Channel, GimpToolkit.main_quit)
    indicator = AppIndicator.Indicator.new(
        'rundfunk_app_indicator_id',
        'gtk-media-play',
        AppIndicator.IndicatorCategory.APPLICATION_STATUS
    )

    indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(app_menu_factory.create())
    GimpToolkit.main()


if __name__ == "__main__":
    main()
