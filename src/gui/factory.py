from src.app import NAME, ICON
from src.event_bus import EventBus
from .g_object import GimpToolkit, AppIndicator
from src.radio import Channel
from .menu import AppMenuFactory, MenuHandler, MenuBuilder
from .mpris import MprisMediaPlayer


def create(event_bus: EventBus) -> None:
    category = AppIndicator.IndicatorCategory.APPLICATION_STATUS
    handler = MenuHandler.create(event_bus, GimpToolkit.main_quit)
    builder = MenuBuilder.create(GimpToolkit, handler)
    factory = AppMenuFactory(builder, Channel)
    indicator = AppIndicator.Indicator.new(NAME, ICON, category)
    mpris_media_player = MprisMediaPlayer(NAME, event_bus)

    mpris_media_player.publish()
    indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(factory.create())
    GimpToolkit.main()
