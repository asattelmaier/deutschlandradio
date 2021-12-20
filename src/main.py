from __future__ import annotations
from g_object import GStreamer, GimpToolkit, AppIndicator
from event_bus import EventBus
from gui import AppMenuFactory, MenuBuilder, MprisAdapter, MenuHandler, EventAdapter, Server
from radio import Radio, Channel, AudioPlayer
from app import NAME, ICON, CATEGORY


def main() -> None:
    current_channel = Channel.DEUTSCHLANDFUNK
    event_bus = EventBus()
    audio_player = AudioPlayer.create(GStreamer)
    Radio.init(audio_player, event_bus, current_channel)
    menu_handler = MenuHandler.create(event_bus)
    menu_builder = MenuBuilder.create(GimpToolkit, menu_handler)
    app_menu_factory = AppMenuFactory(menu_builder, event_bus, Channel, GimpToolkit.main_quit)
    indicator = AppIndicator.Indicator.new(NAME, ICON, CATEGORY)
    mpris_adapter = MprisAdapter.create(event_bus, current_channel)
    mpris_server = Server(NAME, adapter=mpris_adapter)
    mpris_event_adapter = EventAdapter(root=mpris_server.root, player=mpris_server.player)

    # TODO: Optimize mpris_server data flow to avoid setting the event adapter after the instantiation.
    mpris_adapter.set_event_adapter(mpris_event_adapter)
    indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(app_menu_factory.create())

    mpris_server.publish()
    GimpToolkit.main()


if __name__ == "__main__":
    main()
