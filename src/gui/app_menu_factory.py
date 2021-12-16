from src.radio import UpdateChannel
from .menu_item_label import MenuItemLabel


class AppMenuFactory:
    def __init__(self, menu_builder, event_bus, channel, quit_handler):
        self._menu_builder = menu_builder
        self._event_bus = event_bus
        self._channel = channel
        self._quit_handler = quit_handler

    def create(self):
        return self._build_menu()

    def _build_menu(self):
        return self._menu_builder \
            .add_item(MenuItemLabel.DEUTSCHLANDFUNK.value, self._create_deutschlandfunk_item_handler()) \
            .add_item(MenuItemLabel.DEUTSCHLANDFUNK_KULTUR.value, self._create_deutschlandfunk_kultur_item_handler()) \
            .add_item(MenuItemLabel.DEUTSCHLANDFUNK_NOVA.value, self._create_deutschlandfunk_nova_item_handler()) \
            .add_item(MenuItemLabel.DOKUMENTE_UND_DEBATTEN.value, self._create_dokumente_und_debatten_item_handler()) \
            .add_separator() \
            .add_item(MenuItemLabel.QUIT.value, self._quit_handler) \
            .build()

    def _create_deutschlandfunk_item_handler(self):
        return self._create_channel_item_handler(self._channel.DEUTSCHLANDFUNK)

    def _create_deutschlandfunk_kultur_item_handler(self):
        return self._create_channel_item_handler(self._channel.DEUTSCHLANDFUNK_KULTUR)

    def _create_deutschlandfunk_nova_item_handler(self):
        return self._create_channel_item_handler(self._channel.DEUTSCHLANDFUNK_NOVA)

    def _create_dokumente_und_debatten_item_handler(self):
        return self._create_channel_item_handler(self._channel.DOKUMENTE_UND_DEBATTEN)

    def _create_channel_item_handler(self, channel):
        return lambda: self._event_bus.publish(UpdateChannel(channel))
